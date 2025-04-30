#!/usr/bin/env python3

"""
Task 13: Playwright Web Scraping with Error Handling (SOLUTION)

This lesson covers:
- Setting up and using Playwright for web scraping
- Implementing retry logic for error handling
- Saving structured data to JSON files

Complete implementation of all functions.
"""

"""
To run this code, you need to have Playwright installed.

Run the following commands in your terminal:

pip install playwright
python -m playwright install
"""

# Import necessary modules
import asyncio
from playwright.async_api import async_playwright
import json
import time
from typing import Dict, Any, Optional
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define a function to scrape a webpage
async def scrape_webpage(url: str, max_retries: int = 3) -> Optional[Dict[str, Any]]:
    """
    Scrape a webpage and extract its title.
    
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
                
                # Extract h1 headings
                h1_elements = await page.query_selector_all('h1')
                h1_texts = []
                for h1 in h1_elements:
                    h1_text = await h1.inner_text()
                    h1_texts.append(h1_text)
                
                # Close the browser
                await browser.close()
                
                # Return the scraped data
                return {
                    "url": url,
                    "title": title,
                    "description": description,
                    "h1_headings": h1_texts,
                    "timestamp": datetime.now().isoformat()
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

# Define a function to save data to a JSON file
def save_to_json(data: Dict[str, Any], filename: str) -> bool:
    """
    Save data to a JSON file.
    
    Args:
        data (dict): The data to save
        filename (str): The name of the file to save to
        
    Returns:
        bool: True if the data was saved successfully, False otherwise
    """
    try:
        # Ensure filename has .json extension
        if not filename.endswith('.json'):
            filename += '.json'
        
        # Save the data to a JSON file
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Data saved to {filename}")
        return True
    
    except Exception as e:
        # Log the error
        logger.error(f"Error saving data to {filename}: {e}")
        return False

# Define the main async function
async def main_async():
    """
    Main async function to run the scraper.
    """
    # Define the URL to scrape
    url = "https://www.python.org"
    
    logger.info(f"Starting scraping of {url}")
    
    # Call the scrape_webpage function
    data = await scrape_webpage(url)
    
    # If data was returned, save it to a JSON file
    if data:
        # Generate a filename with timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"scrape_result_{timestamp}.json"
        
        # Save the data
        if save_to_json(data, filename):
            logger.info(f"Scraping successful! Data saved to {filename}")
            
            # Print a preview of the data
            print("\nData preview:")
            print(f"URL: {data['url']}")
            print(f"Title: {data['title']}")
            print(f"Description: {data['description'][:100]}..." if len(data['description']) > 100 else f"Description: {data['description']}")
            print(f"H1 Headings: {', '.join(data['h1_headings'][:3])}{'...' if len(data['h1_headings']) > 3 else ''}")
        else:
            logger.error("Failed to save data")
    else:
        logger.error("Scraping failed after all retry attempts")

# Main function to run all tasks
def main():
    print("\n=== Task: Playwright Web Scraping ===\n")
    
    # Run the async function
    asyncio.run(main_async())
    
    print("\nScraping completed!")

# Run the program
if __name__ == "__main__":
    main()
