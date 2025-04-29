#!/usr/bin/env python3

"""
Task 3: Dictionaries, Sets, Tuples

This lesson covers:
- Dictionary creation and access
- Set operations for deduplication
- Tuples for immutable data

Complete the functions below according to the instructions.
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
    # TODO: Implement this function
    # Hint: Create a dictionary with usernames as keys and email addresses as values
    pass


# Task 2: Take a list of email addresses (with duplicates) and print only the unique ones
def unique_emails():
    """
    Take a list of email addresses (with duplicates) and print only the unique ones.
    
    Example:
    Input list: ["user@example.com", "admin@example.com", "user@example.com", "test@test.com"]
    Output: Print only the unique email addresses
    """
    # TODO: Implement this function
    # Hint: Convert the list to a set to remove duplicates
    pass


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
    # TODO: Implement this function
    # Hint: Create a tuple with three elements and access them by index
    pass


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
