#!/usr/bin/env python3

"""
Task 7: FastAPI API Basics (SOLUTION)

This lesson covers:
- Creating a simple FastAPI application
- Defining GET and POST routes
- Testing API endpoints locally

Complete implementation of all functions.
"""

"""
To run this API, you need to have FastAPI installed.

Run the following command in your terminal to install FastAPI and Uvicorn:

pip install fastapi uvicorn

After implementing the code below, you can run the API with:

uvicorn task7_fastapi_basics:app --reload

Then you can access the API at http://localhost:8000
"""

# Import FastAPI and other necessary modules
from fastapi import FastAPI, Body
from pydantic import BaseModel

# Create a FastAPI instance
app = FastAPI(
    title="Simple API",
    description="A simple API with GET and POST routes",
    version="1.0.0"
)

# Define a model for the request body of the POST route
class TextRequest(BaseModel):
    text: str

# Create a GET route at /hello that returns {"message": "Hello World"}
@app.get("/hello")
def hello_world():
    """
    Return a simple greeting message.
    
    Returns:
        dict: A dictionary with a greeting message
    """
    return {"message": "Hello World"}

# Create a POST route at /echo that accepts a JSON body with text, and returns the same text back
@app.post("/echo")
def echo_text(request: TextRequest):
    """
    Echo back the text received in the request body.
    
    Args:
        request (TextRequest): The request body containing text
        
    Returns:
        dict: A dictionary with the echoed text
    """
    return {"text": request.text}

"""
Testing the API:

1. Using curl for the GET route:
   curl http://localhost:8000/hello

2. Using curl for the POST route:
   curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello, FastAPI!"}' http://localhost:8000/echo

3. Using a browser:
   - Open http://localhost:8000/hello in your browser
   - For the POST route, you can use the automatic documentation at http://localhost:8000/docs

4. Additional endpoints provided by FastAPI:
   - Interactive API documentation: http://localhost:8000/docs
   - Alternative API documentation: http://localhost:8000/redoc
   - OpenAPI schema: http://localhost:8000/openapi.json
"""

# If this file is run directly, print instructions
if __name__ == "__main__":
    print("This is a FastAPI application. To run it, use the following command:")
    print("uvicorn task7_fastapi_basics:app --reload")
    print("\nThen access the API at http://localhost:8000/hello")
