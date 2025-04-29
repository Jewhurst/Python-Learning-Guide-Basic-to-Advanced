#!/usr/bin/env python3

"""
Task 1: Basic Syntax, Strings, and Lists (SOLUTION)

This lesson covers:
- Basic input and output
- String operations
- List operations
- Sorting

Complete implementation of all functions.
"""

# Task 1: Write a Python script that asks the user for their name and prints "Hello, [Name]"
def greet_user():
    """
    Ask for the user's name and print a greeting.
    Example: If user enters "John", print "Hello, John".
    """
    name = input("Enter your name: ")
    print(f"Hello, {name}")


# Task 2: Create a list of 5 website URLs as strings. Print each URL on a new line.
def print_urls():
    """
    Create a list of 5 website URLs and print each one on a new line.
    """
    # Create a list of website URLs
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.google.com",
        "https://www.wikipedia.org"
    ]
    
    # Print each URL on a new line
    for url in urls:
        print(url)


# Task 3: Take a single input string of comma-separated tags and output them sorted alphabetically
def sort_tags():
    """
    Ask the user to enter comma-separated tags, then sort and print them alphabetically.
    Example: If user enters "python,programming,code,development", output should be:
    "code,development,programming,python"
    """
    # Get input from user
    tags_input = input("Enter comma-separated tags: ")
    
    # Split the input string by comma
    tags_list = tags_input.split(",")
    
    # Remove any whitespace from the tags
    tags_list = [tag.strip() for tag in tags_list]
    
    # Sort the tags alphabetically
    tags_list.sort()
    
    # Join the sorted tags with commas
    sorted_tags = ",".join(tags_list)
    
    # Print the result
    print(sorted_tags)


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
