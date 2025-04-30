#!/usr/bin/env python3

"""
Task 16: Full App Project (SOLUTION)

This lesson covers building a complete web application that integrates:
- FastAPI for the web server
- Playwright for web scraping
- PostgreSQL for data storage
- Background jobs for data cleanup
- Testing and CI/CD with GitHub Actions

Complete implementation of all functions.
"""

"""
To run this code, you need to have the following installed:

pip install fastapi uvicorn sqlalchemy psycopg2-binary playwright pytest httpx schedule python-dotenv
python -m playwright install

You'll also need PostgreSQL running locally or via Docker.

Docker command to run PostgreSQL:
docker run --name postgres-scraper -e POSTGRES_PASSWORD=password -e POSTGRES_USER=scraper -e POSTGRES_DB=scraper_db -p 5432:5432 -d postgres
"""

# Import necessary modules
from fastapi import FastAPI, HTTPException, Depends, Query, BackgroundTasks
from pydantic import BaseModel, HttpUrl
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Optional, Dict, Any
import asyncio
from playwright.async_api import async_playwright
import schedule
import time
import threading
from datetime import datetime, timedelta
import logging
import os
from dotenv import load_dotenv

# Set up logging
def setup_logging():
    """Configure logging."""
    # Configure logging with a specific format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

# Global logger
logger = setup_logging()

# Load environment variables
def load_environment_variables():
    """Load environment variables from .env file.
    
    Returns:
        str: Database URL
    """
    # Load the .env file
    load_dotenv()
    
    # Get the database URL
    db_url = os.getenv("DATABASE_URL", "postgresql://scraper:password@localhost:5432/scraper_db")
    logger.info(f"Loaded DATABASE_URL from environment")
    
    return db_url

# Create a sample .env file
def create_sample_env_file():
    """Create a sample .env file for testing."""
    # Define the .env file content
    env_content = """
# Database configuration
DATABASE_URL=postgresql://scraper:password@localhost:5432/scraper_db

# Debug mode
DEBUG=True
"""
    
    # Create a .env file with sample variables
    with open(".env", "w") as f:
        f.write(env_content)
    
    logger.info("Created sample .env file")

# Define database models
Base = declarative_base()

class ScrapedPage(Base):
    """SQLAlchemy model for scraped pages."""
    __tablename__ = "scraped_pages"
    
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(2048), nullable=False, index=True)
    title = Column(String(512), nullable=True)
    description = Column(Text, nullable=True)
    content_preview = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

# Set up database connection
def get_db_engine(db_url=None):
    """Create a database engine.
    
    Args:
        db_url (str): Database URL
        
    Returns:
        Engine: SQLAlchemy engine
    """
    if db_url is None:
        db_url = load_environment_variables()
    
    # Create and return a database engine
    engine = create_engine(db_url)
    logger.info(f"Created database engine")
    
    return engine

# Create database tables
def create_tables(engine):
    """Create database tables.
    
    Args:
        engine (Engine): SQLAlchemy engine
    """
    # Create all tables defined in the Base metadata
    Base.metadata.create_all(bind=engine)
    logger.info("Created database tables")

# Create a database session
SessionLocal = None

# Create a database session dependency
def get_db():
    """Get a database session.
    
    Yields:
        Session: SQLAlchemy session
    """
    # Create a database session
    db = SessionLocal()
    try:
        # Yield the session
        yield db
    finally:
        # Close the session when done
        db.close()

# Define Pydantic models for API
class UrlInput(BaseModel):
    """Pydantic model for URL input."""
    url: HttpUrl

class PageOutput(BaseModel):
    """Pydantic model for page output."""
    id: int
    url: str
    title: Optional[str] = None
    description: Optional[str] = None
    content_preview: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

# Define a function to scrape a webpage
async def scrape_webpage(url: str, max_retries: int = 3):
    """Scrape a webpage and extract its title and meta description.
    
    Args:
        url (str): The URL of the webpage to scrape
        max_retries (int): Maximum number of retry attempts
        
    Returns:
        dict or None: A dictionary containing the scraped data, or None if all retries failed
    """
    # Initialize retry counter
    retry_count = 0
    
    # Loop until max_retries is reached
    while retry_count < max_retries:
        try:
            logger.info(f"Attempt {retry_count + 1}/{max_retries} to scrape {url}")
            
            # Start Playwright
            async with async_playwright() as p:
                # Launch a headless browser
                browser = await p.chromium.launch(headless=True)
                
                # Create a new page
                page = await browser.new_page()
                
                # Navigate to the URL
                logger.info(f"Navigating to {url}")
                await page.goto(url, wait_until="networkidle")
                
                # Extract the title
                title = await page.title()
                logger.info(f"Page title: {title}")
                
                # Extract meta description
                description = await page.evaluate("""
                    () => {
                        const metaDescription = document.querySelector('meta[name="description"]');
                        return metaDescription ? metaDescription.getAttribute('content') : '';
                    }
                """)
                
                # Extract a preview of the content (first paragraph)
                content_preview = await page.evaluate("""
                    () => {
                        const paragraph = document.querySelector('p');
                        return paragraph ? paragraph.textContent : '';
                    }
                """)
                
                # Close the browser
                await browser.close()
                
                # Return the scraped data
                return {
                    "url": str(url),
                    "title": title,
                    "description": description,
                    "content_preview": content_preview
                }
                
        except Exception as e:
            # Increment retry counter
            retry_count += 1
            
            # Log the error
            logger.error(f"Error scraping {url} (attempt {retry_count}/{max_retries}): {e}")
            
            # If all retries failed, return None
            if retry_count >= max_retries:
                logger.error(f"All {max_retries} attempts to scrape {url} failed")
                return None
            
            # Wait before retrying (exponential backoff)
            wait_time = 2 ** retry_count
            logger.info(f"Waiting {wait_time} seconds before retrying...")
            await asyncio.sleep(wait_time)

# Define a function to clean up old entries
def cleanup_old_entries(db: Session, days: int = 30):
    """Delete entries older than the specified number of days.
    
    Args:
        db (Session): SQLAlchemy session
        days (int): Number of days to keep entries for
        
    Returns:
        int: Number of deleted entries
    """
    # Calculate the cutoff date
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    logger.info(f"Cleaning up entries older than {cutoff_date}")
    
    # Delete old entries
    result = db.query(ScrapedPage).filter(ScrapedPage.created_at < cutoff_date).delete()
    db.commit()
    
    # Log the result
    logger.info(f"Deleted {result} old entries")
    
    # Return the number of deleted entries
    return result

# Define a function to run the cleanup job
def run_cleanup_job():
    """Run the cleanup job."""
    # Log the job start
    logger.info("Starting cleanup job")
    
    # Create a new database session
    db = SessionLocal()
    
    try:
        # Run the cleanup
        deleted_count = cleanup_old_entries(db)
        logger.info(f"Cleanup job completed. Deleted {deleted_count} old entries.")
    except Exception as e:
        logger.error(f"Error in cleanup job: {e}")
    finally:
        # Close the session
        db.close()

# Define a function to start the background job
def start_background_job():
    """Start the background job to clean up old entries."""
    # Define the job function
    def run_scheduler():
        # Schedule the job to run daily
        schedule.every().day.at("00:00").do(run_cleanup_job)
        
        # For testing, also run every minute
        schedule.every(1).minutes.do(run_cleanup_job)
        
        logger.info("Background job scheduler started")
        
        # Run the job loop
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    # Start the job in a separate thread
    thread = threading.Thread(target=run_scheduler, daemon=True)
    thread.start()
    logger.info("Background job thread started")

# Create the FastAPI app
app = FastAPI(title="Web Scraper API")

# Define the routes
@app.get("/")
def read_root():
    """Root endpoint."""
    # Return a welcome message
    return {"message": "Welcome to the Web Scraper API", "version": "1.0.0"}

@app.post("/scrape", response_model=PageOutput)
async def scrape_url(url_input: UrlInput, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """Endpoint to scrape a URL and save the data."""
    # Scrape the webpage
    scraped_data = await scrape_webpage(str(url_input.url))
    
    if not scraped_data:
        raise HTTPException(status_code=500, detail="Failed to scrape the URL")
    
    # Check if the URL already exists in the database
    existing_page = db.query(ScrapedPage).filter(ScrapedPage.url == scraped_data["url"]).first()
    
    if existing_page:
        # Update the existing page
        existing_page.title = scraped_data["title"]
        existing_page.description = scraped_data["description"]
        existing_page.content_preview = scraped_data["content_preview"]
        existing_page.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(existing_page)
        logger.info(f"Updated existing page: {existing_page.url}")
        return existing_page
    else:
        # Create a new page
        new_page = ScrapedPage(
            url=scraped_data["url"],
            title=scraped_data["title"],
            description=scraped_data["description"],
            content_preview=scraped_data["content_preview"]
        )
        db.add(new_page)
        db.commit()
        db.refresh(new_page)
        logger.info(f"Created new page: {new_page.url}")
        return new_page

@app.get("/pages", response_model=List[PageOutput])
def get_pages(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100), db: Session = Depends(get_db)):
    """Endpoint to get all scraped pages with pagination."""
    # Get the pages from the database with pagination
    pages = db.query(ScrapedPage).order_by(ScrapedPage.created_at.desc()).offset(skip).limit(limit).all()
    return pages

@app.get("/pages/{page_id}", response_model=PageOutput)
def get_page(page_id: int, db: Session = Depends(get_db)):
    """Endpoint to get a specific scraped page."""
    # Get the page from the database
    page = db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()
    
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    
    return page

@app.delete("/pages/{page_id}")
def delete_page(page_id: int, db: Session = Depends(get_db)):
    """Endpoint to delete a specific scraped page."""
    # Get the page from the database
    page = db.query(ScrapedPage).filter(ScrapedPage.id == page_id).first()
    
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    
    # Delete the page
    db.delete(page)
    db.commit()
    
    return {"message": f"Page {page_id} deleted successfully"}

@app.on_event("startup")
async def startup_event():
    """Startup event handler."""
    # Set up logging
    global logger
    logger = setup_logging()
    logger.info("Starting Web Scraper API")
    
    # Load environment variables
    db_url = load_environment_variables()
    
    # Create the database engine
    engine = get_db_engine(db_url)
    
    # Create the database tables
    create_tables(engine)
    
    # Create the session factory
    global SessionLocal
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Start the background job
    start_background_job()
    logger.info("Startup complete")

# Main function to run all tasks
def main():
    print("\n=== Task: Full App Project ===\n")
    
    # Create a sample .env file
    create_sample_env_file()
    
    # Load environment variables
    db_url = load_environment_variables()
    print(f"Database URL: {db_url}")
    
    # Set up the database
    engine = get_db_engine(db_url)
    create_tables(engine)
    
    print("\nTo run the FastAPI app, use the following command:")
    print("uvicorn task16_full_app_project:app --reload")
    
    print("\nTask completed!")

# Run the program
if __name__ == "__main__":
    main()
