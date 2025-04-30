#!/usr/bin/env python3

"""
Task 15: Secure Config and Secrets Management (SOLUTION)

This lesson covers:
- Loading environment variables from .env files
- Basic encryption and decryption using cryptography
- Email validation

Complete implementation of all functions.
"""

"""
To run this code, you need to have the following libraries installed:

pip install python-dotenv cryptography email-validator
"""

# Import necessary modules
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from email_validator import validate_email, EmailNotValidError
import logging
from typing import Dict, List, Tuple, Any

# Set up logging
def setup_logging():
    """Configure logging."""
    # Configure logging with a specific format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

# Create a function to load environment variables
def load_environment_variables() -> Dict[str, str]:
    """Load environment variables from .env file.
    
    Returns:
        dict: Dictionary of environment variables
    """
    # Load the .env file
    load_dotenv()
    logger.info("Loaded environment variables from .env file")
    
    # Get and return the environment variables
    env_vars = {
        "DATABASE_URL": os.getenv("DATABASE_URL", "Not set"),
        "API_KEY": os.getenv("API_KEY", "Not set"),
        "DEBUG": os.getenv("DEBUG", "Not set")
    }
    
    # Log the loaded variables (but mask sensitive values)
    for key, value in env_vars.items():
        if key in ["API_KEY", "DATABASE_URL"]:
            # Mask sensitive values
            masked_value = value[:4] + "*" * (len(value) - 4) if len(value) > 4 else "****"
            logger.info(f"Loaded {key}: {masked_value}")
        else:
            logger.info(f"Loaded {key}: {value}")
    
    return env_vars

# Create a function to generate an encryption key
def generate_encryption_key() -> bytes:
    """Generate a new Fernet encryption key.
    
    Returns:
        bytes: A new Fernet key
    """
    # Generate a new key
    key = Fernet.generate_key()
    logger.info(f"Generated new encryption key")
    
    return key

# Create a function to encrypt a string
def encrypt_string(text: str, key: bytes) -> bytes:
    """Encrypt a string using Fernet.
    
    Args:
        text (str): The text to encrypt
        key (bytes): The encryption key
        
    Returns:
        bytes: The encrypted text
    """
    # Create a Fernet instance with the key
    f = Fernet(key)
    
    # Encrypt the text
    encrypted_text = f.encrypt(text.encode())
    logger.info(f"Encrypted text (length: {len(text)} chars)")
    
    return encrypted_text

# Create a function to decrypt a string
def decrypt_string(encrypted_text: bytes, key: bytes) -> str:
    """Decrypt a string using Fernet.
    
    Args:
        encrypted_text (bytes): The encrypted text
        key (bytes): The encryption key
        
    Returns:
        str: The decrypted text
    """
    # Create a Fernet instance with the key
    f = Fernet(key)
    
    # Decrypt the text
    decrypted_text = f.decrypt(encrypted_text).decode()
    logger.info(f"Decrypted text (length: {len(decrypted_text)} chars)")
    
    return decrypted_text

# Create a function to validate email addresses
def validate_emails(email_list: List[str]) -> Tuple[List[str], List[str]]:
    """Validate a list of email addresses.
    
    Args:
        email_list (list): List of email addresses to validate
        
    Returns:
        tuple: Lists of valid and invalid emails
    """
    # Initialize lists for valid and invalid emails
    valid_emails = []
    invalid_emails = []
    
    # Check each email
    for email in email_list:
        try:
            # Validate the email
            validation = validate_email(email, check_deliverability=False)
            normalized_email = validation.normalized
            
            # Add to valid emails list
            valid_emails.append(normalized_email)
            logger.info(f"Valid email: {email} (normalized: {normalized_email})")
            
        except EmailNotValidError as e:
            # Add to invalid emails list
            invalid_emails.append(email)
            logger.warning(f"Invalid email: {email} - {str(e)}")
    
    # Return the results
    return valid_emails, invalid_emails

# Create a sample .env file
def create_sample_env_file():
    """Create a sample .env file for testing."""
    # Define the .env file content
    env_content = """
# Database configuration
DATABASE_URL=postgresql://user:password@localhost:5432/mydb

# API configuration
API_KEY=sk_test_abcdefghijklmnopqrstuvwxyz123456

# Debug mode
DEBUG=True
"""
    
    # Create a .env file with sample variables
    with open(".env", "w") as f:
        f.write(env_content)
    
    logger.info("Created sample .env file")

# Main function to run all tasks
def main():
    print("\n=== Task: Secure Config and Secrets Management ===\n")
    
    # Set up logging
    global logger
    logger = setup_logging()
    
    # Create a sample .env file
    create_sample_env_file()
    
    # Load environment variables
    env_vars = load_environment_variables()
    print("\nLoaded environment variables:")
    for key, value in env_vars.items():
        if key in ["API_KEY", "DATABASE_URL"]:
            # Mask sensitive values
            masked_value = value[:4] + "*" * (len(value) - 4) if len(value) > 4 else "****"
            print(f"  {key}: {masked_value}")
        else:
            print(f"  {key}: {value}")
    
    # Generate an encryption key
    key = generate_encryption_key()
    print(f"\nGenerated encryption key: {key.decode()}")
    
    # Encrypt and decrypt a string
    secret_message = "This is a secret message that should be encrypted"
    encrypted = encrypt_string(secret_message, key)
    decrypted = decrypt_string(encrypted, key)
    
    print("\nEncryption/Decryption Test:")
    print(f"  Original: {secret_message}")
    print(f"  Encrypted (base64): {encrypted.decode()}")
    print(f"  Decrypted: {decrypted}")
    
    # Validate email addresses
    emails = [
        "user@example.com",
        "invalid-email",
        "another.user@example.com",
        "missing@domain",
        "user@.com"
    ]
    
    valid_emails, invalid_emails = validate_emails(emails)
    
    print("\nEmail Validation Results:")
    print(f"  Valid emails: {', '.join(valid_emails)}")
    print(f"  Invalid emails: {', '.join(invalid_emails)}")
    
    print("\nTask completed!")

# Run the program
if __name__ == "__main__":
    main()
