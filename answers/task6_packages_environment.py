#!/usr/bin/env python3

"""
Task 6: Packages and Environment Setup (SOLUTION)

This lesson covers:
- Creating and activating virtual environments
- Installing packages with pip
- Using environment variables with python-dotenv

Complete implementation of all functions.
"""

# This file provides instructions for setting up a virtual environment and installing packages
# along with the solution for loading environment variables

"""
Step 1: Create a new virtual environment

Run the following command in your terminal:

python -m venv venv


Step 2: Activate the virtual environment

On Windows, run:
venv\Scripts\activate

On macOS/Linux, run:
source venv/bin/activate


Step 3: Install required packages

Run the following command to install the required packages:

pip install requests python-dotenv beautifulsoup4


Step 4: Create a .env file

Create a file named .env in the same directory as this script with the following content:

BASE_URL=https://example.com
"""

# Task: Load an environment variable from the .env file
def load_env_variable():
    """
    Load the BASE_URL environment variable from the .env file and print it.
    
    Steps:
    1. Import the load_dotenv function from dotenv
    2. Import the os module to access environment variables
    3. Call load_dotenv() to load variables from .env file
    4. Get and print the BASE_URL environment variable
    """
    # Import required modules
    from dotenv import load_dotenv
    import os
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the BASE_URL environment variable
    base_url = os.getenv("BASE_URL")
    
    # Print the BASE_URL
    if base_url:
        print(f"BASE_URL: {base_url}")
    else:
        print("BASE_URL environment variable not found. Make sure you have created a .env file with BASE_URL=https://example.com")
    
    return base_url


# Additional example: Using the requests package
def example_requests_usage():
    """
    Example of using the requests package to make an HTTP request.
    """
    try:
        import requests
        
        # Get the BASE_URL from environment variables
        from dotenv import load_dotenv
        import os
        load_dotenv()
        base_url = os.getenv("BASE_URL", "https://example.com")
        
        # Make a GET request
        response = requests.get(base_url)
        
        # Print the response status code and content
        print(f"\nMaking a GET request to {base_url}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content length: {len(response.text)} characters")
        print(f"Response content (first 100 chars): {response.text[:100]}...")
        
    except ImportError:
        print("\nThe requests package is not installed. Run 'pip install requests' to install it.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


# Additional example: Using the BeautifulSoup package
def example_beautifulsoup_usage():
    """
    Example of using the BeautifulSoup package to parse HTML.
    """
    try:
        import requests
        from bs4 import BeautifulSoup
        
        # Get the BASE_URL from environment variables
        from dotenv import load_dotenv
        import os
        load_dotenv()
        base_url = os.getenv("BASE_URL", "https://example.com")
        
        # Make a GET request
        response = requests.get(base_url)
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Print the page title
        print(f"\nParsing HTML content from {base_url}")
        print(f"Page title: {soup.title.string}")
        
        # Print all links on the page
        print("\nLinks found on the page:")
        for i, link in enumerate(soup.find_all('a', href=True), 1):
            print(f"{i}. {link.get('href')}")
            if i >= 5:  # Limit to 5 links
                print("...and more")
                break
        
    except ImportError as e:
        print(f"\nRequired package not installed: {e}. Run 'pip install requests beautifulsoup4' to install them.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


# Main function to run the task
def main():
    print("\n=== Task: Load Environment Variable ===\n")
    base_url = load_env_variable()
    
    if base_url:
        print("\n=== Additional Examples (Optional) ===")
        example_requests_usage()
        example_beautifulsoup_usage()


# Run the program
if __name__ == "__main__":
    main()
