#!/usr/bin/env python3

"""
Task 3: Dictionaries, Sets, Tuples (SOLUTION)

This lesson covers:
- Dictionary creation and access
- Set operations for deduplication
- Tuples for immutable data

Complete implementation of all functions.
"""

# Task 1: Create a dictionary with three users and their email addresses
def user_emails():
    """
    Create a dictionary with three users and their email addresses.
    Print each user's name and email address.
    
    Example output format:
    User: John
    Email: john@example.com
    
    User: Sarah
    Email: sarah@example.com
    
    User: Mike
    Email: mike@example.com
    """
    # Create a dictionary with usernames as keys and email addresses as values
    users = {
        "John": "john@example.com",
        "Sarah": "sarah@example.com",
        "Mike": "mike@example.com"
    }
    
    # Print each user's name and email address
    for username, email in users.items():
        print(f"User: {username}")
        print(f"Email: {email}")
        print()  # Empty line for better readability


# Task 2: Take a list of email addresses (with duplicates) and print only the unique ones
def unique_emails():
    """
    Take a list of email addresses (with duplicates) and print only the unique ones.
    
    Example:
    Input list: ["user@example.com", "admin@example.com", "user@example.com", "test@test.com"]
    Output: Print only the unique email addresses
    """
    # Create a list of email addresses (with duplicates)
    emails = [
        "user@example.com",
        "admin@example.com",
        "user@example.com",
        "test@test.com",
        "admin@example.com",
        "support@example.com"
    ]
    
    # Print the original list
    print("Original email list:")
    for email in emails:
        print(f"- {email}")
    
    # Convert the list to a set to remove duplicates
    unique_email_set = set(emails)
    
    # Print the unique emails
    print("\nUnique emails:")
    for email in unique_email_set:
        print(f"- {email}")


# Task 3: Create a tuple to store a username, user ID, and a creation date
def user_info_tuple():
    """
    Create a tuple to store a username, user ID, and a creation date.
    Print each value from the tuple.
    
    Example output format:
    Username: johndoe
    User ID: 12345
    Creation Date: 2023-04-15
    """
    # Create a tuple with username, user ID, and creation date
    user_info = ("johndoe", 12345, "2023-04-15")
    
    # Print each value from the tuple
    print(f"Username: {user_info[0]}")
    print(f"User ID: {user_info[1]}")
    print(f"Creation Date: {user_info[2]}")
    
    # Demonstrate tuple unpacking (alternative approach)
    print("\nUsing tuple unpacking:")
    username, user_id, creation_date = user_info
    print(f"Username: {username}")
    print(f"User ID: {user_id}")
    print(f"Creation Date: {creation_date}")
    
    # Demonstrate that tuples are immutable
    print("\nDemonstrating tuple immutability:")
    try:
        print("Attempting to modify the tuple...")
        user_info[0] = "newusername"  # This will raise a TypeError
    except TypeError as e:
        print(f"Error: {e}")
        print("This demonstrates that tuples are immutable!")


# Main function to run all tasks
def main():
    print("\n=== Task 1: User Emails Dictionary ===\n")
    user_emails()
    
    print("\n=== Task 2: Unique Emails ===\n")
    unique_emails()
    
    print("\n=== Task 3: User Info Tuple ===\n")
    user_info_tuple()


# Run the program
if __name__ == "__main__":
    main()
