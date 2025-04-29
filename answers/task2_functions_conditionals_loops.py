#!/usr/bin/env python3

"""
Task 2: Loops, Conditionals, and Functions (SOLUTION)

This lesson covers:
- Function definition and return values
- For loops and range()
- Conditional statements (if/else)
- Input validation logic

Complete implementation of all functions.
"""

# Task 1: Write a function that takes a number and returns True if it's even, otherwise False
def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if the number is even, False otherwise
    """
    # Check if the number is divisible by 2
    return number % 2 == 0


# Task 2: Print numbers from 1 to 20, skipping numbers that are divisible by 3
def print_numbers_skip_divisible_by_three():
    """
    Print numbers from 1 to 20, but skip any number that is divisible by 3.
    
    Expected output:
    1
    2
    4
    5
    7
    8
    10
    ...and so on (excluding 3, 6, 9, 12, 15, 18)
    """
    # Loop through numbers 1 to 20
    for num in range(1, 21):
        # Skip numbers divisible by 3
        if num % 3 == 0:
            continue
        # Print the number
        print(num)


# Task 3: Ask the user to enter a password and validate it
def validate_password():
    """
    Ask the user to enter a password and check that it's at least 8 characters
    and contains at least one number. Print a success or failure message.
    
    Password requirements:
    - At least 8 characters long
    - Contains at least one number (0-9)
    """
    # Get password from user
    password = input("Enter a password: ")
    
    # Check password length
    if len(password) < 8:
        print("Password failed: Must be at least 8 characters long.")
        return
    
    # Check if password contains at least one number
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    
    # Print result based on validation
    if has_number:
        print("Password accepted: Meets all requirements!")
    else:
        print("Password failed: Must contain at least one number.")





# Main function to run all tasks
def main():
    print("\n=== Task 1: Even Number Checker ===\n")
    test_numbers = [1, 2, 7, 10, 15, 22]
    for num in test_numbers:
        result = is_even(num)
        print(f"Is {num} even? {result}")
    
    print("\n=== Task 2: Print Numbers (Skip Divisible by 3) ===\n")
    print_numbers_skip_divisible_by_three()
    
    print("\n=== Task 3: Password Validation ===\n")
    validate_password()


# Run the program
if __name__ == "__main__":
    main()
