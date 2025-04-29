#!/usr/bin/env python3

"""
Task 1: Basic Syntax, Strings, and Lists

This lesson covers:
- Basic input and output
- String operations
- List operations
- Sorting

Complete the functions below according to the instructions.
"""

# Task 1: Write a Python script that asks the user for their name and prints "Hello, [Name]"
def greet_user():
    """
    Ask for the user's name and print a greeting.
    Example: If user enters "John", print "Hello, John".
    """
    # TODO: Implement this function
    # Hint: Use input() to get user input and print() to display output
    pass


# Task 2: Create a list of 5 website URLs as strings. Print each URL on a new line.
def print_urls():
    """
    Create a list of 5 website URLs and print each one on a new line.
    """
    # TODO: Implement this function
    # Hint: Create a list of URLs and use a loop to print each one
    pass


# Task 3: Take a single input string of comma-separated tags and output them sorted alphabetically
def sort_tags():
    """
    Ask the user to enter comma-separated tags, then sort and print them alphabetically.
    Example: If user enters "python,programming,code,development", output should be:
    "code,development,programming,python"
    """
    # TODO: Implement this function
    # Hint: Use string split(), sort a list, and join() to create the output
    pass


# Main function to run all tasks
def main():
    print("\n=== Task 1: Greeting ===\n")
    greet_user()
    
    print("\n=== Task 2: Website URLs ===\n")
    print_urls()
    
    print("\n=== Task 3: Sort Tags ===\n")
    sort_tags()


# Run the program
if __name__ == "__main__":
    main()
