#!/usr/bin/env python3

"""
Task 12: Mocking and GitHub Actions

This lesson covers:
- Writing tests with pytest
- Mocking external API calls
- Setting up GitHub Actions for CI

Complete the functions and tests below according to the instructions.
"""

"""
To complete this task, you need to have pytest and requests installed.

Run the following command in your terminal:

pip install pytest requests

After implementing the code below, you can run the tests with:

python -m pytest task12_mocking_github_actions.py -v
"""

# TODO: Import necessary modules
# import requests
# import pytest
# from unittest.mock import patch, MagicMock

# A simple function that makes an API call
def get_user_data(user_id):
    """
    Get user data from an external API.
    
    Args:
        user_id (int): The ID of the user to fetch
        
    Returns:
        dict: The user data if successful, None otherwise
    """
    # TODO: Implement this function
    # Make a GET request to the API
    # Return the JSON response if successful, None otherwise
    pass

# TODO: Write a test that mocks the API call
# def test_get_user_data():
#     """Test the get_user_data function with a mocked API response."""
#     # Create a mock response with fake user data
#     # Patch the requests.get function to return the mock response
#     # Call the get_user_data function
#     # Assert that the function returns the expected data
#     pass

# TODO: Write a test that intentionally fails (for GitHub Actions demonstration)
# def test_intentional_failure():
#     """This test will fail to demonstrate GitHub Actions failure detection."""
#     # Uncomment the line below to make the test fail
#     # assert False, "This test is intentionally failing"
#     pass

"""
GitHub Actions Setup:

1. Create a .github/workflows directory in your repository:
   mkdir -p .github/workflows

2. Create a test.yml file in that directory with the following content:

name: Python Tests

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

3. Push your code to GitHub and check the Actions tab to see the workflow run.

4. To demonstrate a failure, uncomment the assertion in test_intentional_failure,
   push the change, and observe the workflow failure in GitHub Actions.

5. Fix the test by commenting out the assertion again, push the change,
   and observe the workflow success.
"""

# If this file is run directly, run the tests
if __name__ == "__main__":
    print("This file contains tests. Run them with: python -m pytest task12_mocking_github_actions.py -v")
