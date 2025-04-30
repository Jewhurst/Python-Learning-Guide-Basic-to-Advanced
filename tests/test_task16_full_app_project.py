#!/usr/bin/env python3

"""
Tests for Task 16: Full App Project

This file contains tests for the FastAPI application in task16_full_app_project.py.
"""

import sys
import os
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Add the parent directory to the path so we can import the task module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the app and models from the task module
from answers.task16_full_app_project import app, ScrapedPage, Base, get_db

# Create an in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///:memory:"

# Create a test engine
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

# Create the tables
Base.metadata.create_all(bind=engine)

# Create a test session
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the dependency in the app
app.dependency_overrides[get_db] = override_get_db

# Create a test client
client = TestClient(app)

# Sample data for tests
sample_page_data = {
    "url": "https://www.example.com",
    "title": "Example Domain",
    "description": "This domain is for use in illustrative examples in documents.",
    "content_preview": "This domain is established to be used for illustrative examples in documents."
}

# Mock response for the scrape_webpage function
mock_scrape_result = {
    "url": "https://www.example.com",
    "title": "Example Domain",
    "description": "This domain is for use in illustrative examples in documents.",
    "content_preview": "This domain is established to be used for illustrative examples in documents."
}

# Test the root endpoint
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "version" in response.json()

# Test the scrape endpoint with a mock
@patch("answers.task16_full_app_project.scrape_webpage")
async def mock_scrape_webpage(*args, **kwargs):
    return mock_scrape_result

@pytest.mark.asyncio
@patch("answers.task16_full_app_project.scrape_webpage", return_value=mock_scrape_result)
async def test_scrape_url(mock_scrape):
    response = client.post(
        "/scrape",
        json={"url": "https://www.example.com"}
    )
    assert response.status_code == 200
    assert response.json()["url"] == "https://www.example.com"
    assert response.json()["title"] == "Example Domain"
    assert "description" in response.json()
    assert "content_preview" in response.json()
    assert "created_at" in response.json()
    assert "updated_at" in response.json()

# Test the get_pages endpoint
def test_get_pages():
    # Add some test data
    db = TestingSessionLocal()
    for i in range(5):
        page = ScrapedPage(
            url=f"https://example.com/{i}",
            title=f"Example Page {i}",
            description=f"Description {i}",
            content_preview=f"Content {i}",
            created_at=datetime.utcnow() - timedelta(days=i)
        )
        db.add(page)
    db.commit()
    
    # Test with default pagination
    response = client.get("/pages")
    assert response.status_code == 200
    assert len(response.json()) <= 10  # Default limit is 10
    
    # Test with custom pagination
    response = client.get("/pages?skip=2&limit=2")
    assert response.status_code == 200
    assert len(response.json()) == 2
    
    # Clean up
    db.query(ScrapedPage).delete()
    db.commit()
    db.close()

# Test the get_page endpoint
def test_get_page():
    # Add a test page
    db = TestingSessionLocal()
    page = ScrapedPage(
        url="https://example.com/test",
        title="Test Page",
        description="Test Description",
        content_preview="Test Content"
    )
    db.add(page)
    db.commit()
    db.refresh(page)
    page_id = page.id
    
    # Test getting the page
    response = client.get(f"/pages/{page_id}")
    assert response.status_code == 200
    assert response.json()["id"] == page_id
    assert response.json()["url"] == "https://example.com/test"
    
    # Test getting a non-existent page
    response = client.get("/pages/999")
    assert response.status_code == 404
    
    # Clean up
    db.delete(page)
    db.commit()
    db.close()

# Test the delete_page endpoint
def test_delete_page():
    # Add a test page
    db = TestingSessionLocal()
    page = ScrapedPage(
        url="https://example.com/delete",
        title="Delete Page",
        description="Delete Description",
        content_preview="Delete Content"
    )
    db.add(page)
    db.commit()
    db.refresh(page)
    page_id = page.id
    
    # Test deleting the page
    response = client.delete(f"/pages/{page_id}")
    assert response.status_code == 200
    assert "message" in response.json()
    
    # Verify the page was deleted
    response = client.get(f"/pages/{page_id}")
    assert response.status_code == 404
    
    # Test deleting a non-existent page
    response = client.delete("/pages/999")
    assert response.status_code == 404
    
    db.close()

# Test the cleanup_old_entries function
def test_cleanup_old_entries():
    from answers.task16_full_app_project import cleanup_old_entries
    
    # Add some test pages with different dates
    db = TestingSessionLocal()
    
    # Add 3 old pages (40 days old)
    old_date = datetime.utcnow() - timedelta(days=40)
    for i in range(3):
        page = ScrapedPage(
            url=f"https://example.com/old/{i}",
            title=f"Old Page {i}",
            description=f"Old Description {i}",
            content_preview=f"Old Content {i}",
            created_at=old_date
        )
        db.add(page)
    
    # Add 2 new pages (10 days old)
    new_date = datetime.utcnow() - timedelta(days=10)
    for i in range(2):
        page = ScrapedPage(
            url=f"https://example.com/new/{i}",
            title=f"New Page {i}",
            description=f"New Description {i}",
            content_preview=f"New Content {i}",
            created_at=new_date
        )
        db.add(page)
    
    db.commit()
    
    # Run the cleanup function (30 days)
    deleted_count = cleanup_old_entries(db, days=30)
    
    # Verify that only the old pages were deleted
    assert deleted_count == 3
    
    # Verify that the new pages still exist
    remaining_pages = db.query(ScrapedPage).all()
    assert len(remaining_pages) == 2
    
    # Clean up
    db.query(ScrapedPage).delete()
    db.commit()
    db.close()
