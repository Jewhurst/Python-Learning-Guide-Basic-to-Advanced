#!/usr/bin/env python3

"""
Task 6: Packages and Environment Setup

This lesson covers:
- Creating and activating virtual environments
- Installing packages with pip
- Using environment variables with python-dotenv

Complete the steps below according to the instructions.
"""

# This file provides instructions for setting up a virtual environment and installing packages
# Follow the steps below and complete the load_env_variable() function

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
    # TODO: Implement this function
    # Hint: Use load_dotenv() and os.getenv()
    pass


# Main function to run the task
def main():
    print("\n=== Task: Load Environment Variable ===\n")
    load_env_variable()


# Run the program
if __name__ == "__main__":
    main()
