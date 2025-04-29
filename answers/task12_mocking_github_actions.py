#!/usr/bin/env python3

"""
Task 12: Mocking and GitHub Actions (SOLUTION)

This lesson covers:
- Writing tests with pytest
- Mocking external API calls
- Setting up GitHub Actions for CI

Complete implementation of all functions and tests.
"""

"""
To run this code, you need to have pytest and requests installed.

Run the following command in your terminal:

pip install pytest requests

After implementing the code below, you can run the tests with:

python -m pytest task12_mocking_github_actions.py -v
"""

# Import necessary modules
import requests
import pytest
from unittest.mock import patch, MagicMock

# A simple function that makes an API call
def get_user_data(user_id):
    """
    Get user data from an external API.
    
    Args:
        user_id (int): The ID of the user to fetch
        
    Returns:
        dict: The user data if successful, None otherwise
    """
    try:
        # Make a GET request to the API
        response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: API returned status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching user data: {e}")
        return None

# Test that mocks the API call
def test_get_user_data():
    """
    Test the get_user_data function with a mocked API response.
    
    This test demonstrates how to mock an external API call to avoid making
    actual network requests during testing.
    """
    # Create a mock response with fake user data
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "id": 1,
        "name": "John Doe",
        "username": "johndoe",
        "email": "john@example.com",
        "phone": "123-456-7890",
        "website": "johndoe.com"
    }
    
    # Patch the requests.get function to return the mock response
    with patch('requests.get', return_value=mock_response) as mock_get:
        # Call the get_user_data function
        result = get_user_data(1)
        
        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")
        
        # Assert that the function returns the expected data
        assert result is not None
        assert result["id"] == 1
        assert result["name"] == "John Doe"
        assert result["email"] == "john@example.com"

# Test that mocks an error response
def test_get_user_data_error():
    """
    Test the get_user_data function with a mocked error response.
    
    This test demonstrates how to mock an API error response.
    """
    # Create a mock response for an error
    mock_response = MagicMock()
    mock_response.status_code = 404  # Not Found
    
    # Patch the requests.get function to return the mock error response
    with patch('requests.get', return_value=mock_response) as mock_get:
        # Call the get_user_data function
        result = get_user_data(999)  # Non-existent user ID
        
        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/999")
        
        # Assert that the function returns None for an error response
        assert result is None

# Test that mocks a network exception
def test_get_user_data_exception():
    """
    Test the get_user_data function with a mocked network exception.
    
    This test demonstrates how to mock a network exception.
    """
    # Patch the requests.get function to raise an exception
    with patch('requests.get', side_effect=requests.exceptions.ConnectionError("Connection refused")) as mock_get:
        # Call the get_user_data function
        result = get_user_data(1)
        
        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")
        
        # Assert that the function returns None for an exception
        assert result is None

# Test that intentionally fails (for GitHub Actions demonstration)
def test_intentional_failure():
    """
    This test will fail to demonstrate GitHub Actions failure detection.
    
    Uncomment the assertion below to make the test fail, then push to GitHub
    to see the workflow fail. Comment it again to make the test pass.
    """
    # Uncomment the line below to make the test fail
    # assert False, "This test is intentionally failing"
    pass

"""
GitHub Actions Setup:

1. Create a .github/workflows directory in your repository:
   mkdir -p .github/workflows

2. Create a test.yml file in that directory with the following content:
"""

# Create the GitHub Actions workflow file
def create_github_workflow_file():
    """
    Create the GitHub Actions workflow file for CI.
    
    This function is not meant to be run automatically. Call it manually
    to create the workflow file in the correct location.
    """
    import os
    
    # Create the workflows directory if it doesn't exist
    os.makedirs(".github/workflows", exist_ok=True)
    
    # Define the workflow file content
    workflow_content = """name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest requests
    - name: Test with pytest
      run: |
        pytest
"""
    
    # Write the workflow file
    with open(".github/workflows/test.yml", "w") as f:
        f.write(workflow_content)
    
    print("GitHub Actions workflow file created at .github/workflows/test.yml")

# If this file is run directly, run the tests
if __name__ == "__main__":
    print("This file contains tests. Run them with: python -m pytest task12_mocking_github_actions.py -v")
    
    # Uncomment the line below to create the GitHub Actions workflow file
    # create_github_workflow_file()
