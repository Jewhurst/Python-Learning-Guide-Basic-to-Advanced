#!/usr/bin/env python3

"""
Task 11: Auth and Pagination in FastAPI (SOLUTION)

This lesson covers:
- Creating login routes with token-based authentication
- Protecting routes with authentication
- Implementing pagination for API responses

Complete implementation of all functions.
"""

"""
To run this code, you need to have FastAPI and uvicorn installed.

Run the following command in your terminal:

pip install fastapi uvicorn

After implementing the code below, you can run the API with:

uvicorn task11_fastapi_auth_pagination:app --reload

Then you can access the API at http://localhost:8000
"""

# Import necessary modules
from fastapi import FastAPI, Depends, HTTPException, Header, Query, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uuid

# Create a FastAPI instance
app = FastAPI(
    title="Auth and Pagination API",
    description="A FastAPI application demonstrating authentication and pagination",
    version="1.0.0"
)

# Define models for request and response
class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    password: str

class Item(BaseModel):
    id: int
    name: str
    description: str

# Create a dictionary to store tokens
tokens: Dict[str, str] = {}  # token -> username

# Create a function to generate fake items
def generate_items(count: int = 50) -> List[Item]:
    """Generate a list of fake items."""
    items = []
    for i in range(1, count + 1):
        items.append(Item(
            id=i,
            name=f"Item {i}",
            description=f"This is the description for item {i}"
        ))
    return items

# Create a function to verify the token
async def verify_token(authorization: Optional[str] = Header(None)) -> str:
    """Verify the token from the Authorization header."""
    # Check if the Authorization header exists
    if not authorization:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Extract the token from the header (remove 'Bearer ' prefix)
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization header format",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Check if the token is valid
    if token not in tokens:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Return the username if the token is valid
    return tokens[token]

# Create a login route
@app.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login route that accepts username and password and returns a token."""
    # Check if the username and password are valid (for simplicity, accept any non-empty values)
    username = form_data.username
    password = form_data.password
    
    if not username or not password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    # Generate a token (UUID)
    token = str(uuid.uuid4())
    
    # Store the token with the username
    tokens[token] = username
    
    # Return the token
    return Token(access_token=token, token_type="bearer")

# Create a protected route
@app.get("/protected")
async def protected_route(username: str = Depends(verify_token)):
    """Protected route that requires a valid token."""
    # Return a message with the username
    return {"message": f"Hello, {username}! This is a protected route."}

# Create a paginated items route
@app.get("/items")
async def get_items(
    page: int = Query(1, gt=0, description="Page number, starting from 1"),
    size: int = Query(10, gt=0, le=100, description="Number of items per page")
):
    """Return a paginated list of items."""
    # Generate a list of items
    all_items = generate_items(50)
    
    # Calculate the start and end indices for pagination
    start_idx = (page - 1) * size
    end_idx = start_idx + size
    
    # Get the paginated items
    paginated_items = all_items[start_idx:end_idx]
    
    # Calculate total pages
    total_items = len(all_items)
    total_pages = (total_items + size - 1) // size  # Ceiling division
    
    # Return the paginated items and metadata
    return {
        "items": paginated_items,
        "metadata": {
            "page": page,
            "size": size,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_prev": page > 1
        }
    }

# Root route for API information
@app.get("/")
async def root():
    """Root route with API information."""
    return {
        "message": "Welcome to the Auth and Pagination API",
        "endpoints": {
            "/login": "POST - Get an authentication token",
            "/protected": "GET - Access a protected route (requires token)",
            "/items": "GET - Get a paginated list of items"
        },
        "documentation": "/docs"
    }

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
