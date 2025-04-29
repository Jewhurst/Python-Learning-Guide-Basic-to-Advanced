#!/usr/bin/env python3

"""
Task 11: Auth and Pagination in FastAPI

This lesson covers:
- Creating login routes with token-based authentication
- Protecting routes with authentication
- Implementing pagination for API responses

Complete the functions below according to the instructions.
"""

"""
To complete this task, you need to have FastAPI and uvicorn installed.

Run the following command in your terminal:

pip install fastapi uvicorn

After implementing the code below, you can run the API with:

uvicorn task11_fastapi_auth_pagination:app --reload

Then you can access the API at http://localhost:8000
"""

# TODO: Import necessary modules
# from fastapi import FastAPI, Depends, HTTPException, Header, Query
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from pydantic import BaseModel
# from typing import List, Optional
# import uuid

# TODO: Create a FastAPI instance
# app = FastAPI()

# TODO: Define models for request and response
# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class User(BaseModel):
#     username: str
#     password: str

# class Item(BaseModel):
#     id: int
#     name: str
#     description: str

# TODO: Create a dictionary to store tokens
# tokens = {}

# TODO: Create a function to generate fake items
# def generate_items(count: int = 50) -> List[Item]:
#     """Generate a list of fake items."""
#     # Generate and return a list of Item objects
#     pass

# TODO: Create a function to verify the token
# async def verify_token(authorization: Optional[str] = Header(None)) -> str:
#     """Verify the token from the Authorization header."""
#     # Check if the Authorization header exists
#     # Extract the token from the header (remove 'Bearer ' prefix)
#     # Check if the token is valid
#     # Return the username if the token is valid
#     # Raise an HTTPException if the token is invalid
#     pass

# TODO: Create a login route
# @app.post("/login", response_model=Token)
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     """Login route that accepts username and password and returns a token."""
#     # Check if the username and password are valid (for simplicity, accept any non-empty values)
#     # Generate a token (UUID)
#     # Store the token with the username
#     # Return the token
#     pass

# TODO: Create a protected route
# @app.get("/protected")
# async def protected_route(username: str = Depends(verify_token)):
#     """Protected route that requires a valid token."""
#     # Return a message with the username
#     pass

# TODO: Create a paginated items route
# @app.get("/items")
# async def get_items(page: int = Query(1, gt=0), size: int = Query(10, gt=0, le=100)):
#     """Return a paginated list of items."""
#     # Generate a list of items
#     # Calculate the start and end indices for pagination
#     # Return the paginated items and metadata
#     pass

"""
Testing the API:

1. Login and get a token:
   curl -X POST "http://localhost:8000/login" -d "username=testuser&password=password"

2. Access the protected route with the token:
   curl -X GET "http://localhost:8000/protected" -H "Authorization: Bearer YOUR_TOKEN"

3. Get paginated items:
   curl -X GET "http://localhost:8000/items?page=1&size=10"

4. Try different pagination parameters:
   curl -X GET "http://localhost:8000/items?page=2&size=5"
"""

# If this file is run directly, print instructions
if __name__ == "__main__":
    print("This is a FastAPI application with auth and pagination.")
    print("To run the API: uvicorn task11_fastapi_auth_pagination:app --reload")
    print("Then access the API at http://localhost:8000/docs")
