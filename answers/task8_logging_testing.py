#!/usr/bin/env python3

"""
Task 8: Logging and Testing (SOLUTION)

This lesson covers:
- Adding logging to a FastAPI application
- Writing tests with pytest
- Testing API endpoints

Complete implementation of all functions.
"""

"""
To run this code, you need to have FastAPI, pytest, and colorlog installed.

Run the following command in your terminal:

pip install fastapi uvicorn pytest pytest-asyncio httpx colorlog

After implementing the code below, you can run the API with:

uvicorn task8_logging_testing:app --reload

And run the tests with:

python -m pytest task8_logging_testing.py -v
"""

# Import necessary modules
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
import logging
import colorlog
import pytest
from pydantic import BaseModel

# Configure colorlog
def setup_logger():
    """Configure and return a logger with colored output."""
    # Create a handler
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )
    )
    
    # Create a logger
    logger = logging.getLogger("api")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    return logger

# Create a logger
logger = setup_logger()

# Create a FastAPI instance
app = FastAPI(
    title="API with Logging",
    description="A FastAPI application with logging and tests",
    version="1.0.0"
)

# Define a model for the request body
class TextRequest(BaseModel):
    text: str

# Add middleware to log every request
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log every request path."""
    # Log the request path
    logger.info(f"Request path: {request.url.path}")
    
    # Call the next middleware/route handler
    response = await call_next(request)
    
    # Log the response status code
    logger.info(f"Response status code: {response.status_code}")
    
    # Return the response
    return response

# Create a GET route at /hello
@app.get("/hello")
def hello_world():
    """Return a hello world message."""
    logger.info("Hello endpoint called")
    return {"message": "Hello World"}

# Create a POST route at /echo
@app.post("/echo")
def echo_text(request: TextRequest):
    """Echo back the text received in the request."""
    logger.info(f"Echo endpoint called with text: {request.text}")
    return {"text": request.text}

# Create a test client
client = TestClient(app)

# Write a test for the GET route
def test_hello_endpoint():
    """Test that /hello returns a 200 status code and the correct message."""
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Write a test for the POST route
def test_echo_endpoint():
    """Test that /echo returns the same text that was sent."""
    test_text = "Hello, FastAPI!"
    response = client.post("/echo", json={"text": test_text})
    assert response.status_code == 200
    assert response.json() == {"text": test_text}

"""
Running the tests:

python -m pytest task8_logging_testing.py -v

You should see output like:

test_hello_endpoint PASSED
test_echo_endpoint PASSED
"""

# If this file is run directly, print instructions
if __name__ == "__main__":
    print("This is a FastAPI application with logging and tests.")
    print("To run the API: uvicorn task8_logging_testing:app --reload")
    print("To run the tests: python -m pytest task8_logging_testing.py -v")
