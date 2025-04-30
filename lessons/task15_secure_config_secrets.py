#!/usr/bin/env python3

"""
Task 15: Secure Config and Secrets Management

This lesson covers:
- Loading environment variables from .env files
- Basic encryption and decryption using cryptography
- Email validation

Complete the functions below according to the instructions.
"""

"""
To complete this task, you need to have the following libraries installed:

pip install python-dotenv cryptography email-validator
"""

# TODO: Import necessary modules
# import os
# from dotenv import load_dotenv
# from cryptography.fernet import Fernet
# from email_validator import validate_email, EmailNotValidError
# import logging

# TODO: Set up logging
# def setup_logging():
#     """Configure logging."""
#     # Configure logging with a specific format
#     pass

# TODO: Create a function to load environment variables
# def load_environment_variables():
#     """Load environment variables from .env file."""
#     # Load the .env file
#     # Get and return the environment variables
#     pass

# TODO: Create a function to generate an encryption key
# def generate_encryption_key():
#     """Generate a new Fernet encryption key."""
#     # Generate a new key
#     # Return the key
#     pass

# TODO: Create a function to encrypt a string
# def encrypt_string(text, key):
#     """Encrypt a string using Fernet."""
#     # Create a Fernet instance with the key
#     # Encrypt the text
#     # Return the encrypted text
#     pass

# TODO: Create a function to decrypt a string
# def decrypt_string(encrypted_text, key):
#     """Decrypt a string using Fernet."""
#     # Create a Fernet instance with the key
#     # Decrypt the text
#     # Return the decrypted text
#     pass

# TODO: Create a function to validate email addresses
# def validate_emails(email_list):
#     """Validate a list of email addresses."""
#     # Initialize lists for valid and invalid emails
#     # Check each email
#     # Return the results
#     pass

# TODO: Create a sample .env file
# def create_sample_env_file():
#     """Create a sample .env file for testing."""
#     # Create a .env file with sample variables
#     pass

# Main function to run all tasks
def main():
    print("\n=== Task: Secure Config and Secrets Management ===\n")
    
    # TODO: Set up logging
    # logger = setup_logging()
    
    # TODO: Create a sample .env file
    # create_sample_env_file()
    
    # TODO: Load environment variables
    # env_vars = load_environment_variables()
    # print(f"Loaded environment variables: {env_vars}")
    
    # TODO: Generate an encryption key
    # key = generate_encryption_key()
    # print(f"Generated encryption key: {key}")
    
    # TODO: Encrypt and decrypt a string
    # secret_message = "This is a secret message that should be encrypted"
    # encrypted = encrypt_string(secret_message, key)
    # decrypted = decrypt_string(encrypted, key)
    # print(f"Original: {secret_message}")
    # print(f"Encrypted: {encrypted}")
    # print(f"Decrypted: {decrypted}")
    
    # TODO: Validate email addresses
    # emails = [
    #     "user@example.com",
    #     "invalid-email",
    #     "another.user@example.com",
    #     "missing@domain",
    #     "user@.com"
    # ]
    # valid_emails, invalid_emails = validate_emails(emails)
    # print(f"Valid emails: {valid_emails}")
    # print(f"Invalid emails: {invalid_emails}")
    
    print("\nTask completed!")

# Run the program
if __name__ == "__main__":
    main()
