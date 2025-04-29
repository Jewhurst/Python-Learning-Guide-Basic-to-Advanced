#!/usr/bin/env python3

"""
Task 4: File I/O and Error Handling

This lesson covers:
- Reading from files
- Writing to files
- Exception handling with try/except

Complete the functions below according to the instructions.
"""

# Task 1: Open a text file and count lines containing a specific word
def count_error_lines():
    """
    Open a text file called input.txt. Read all the lines and count how many lines
    contain the word "error".
    
    Returns:
        int: The number of lines containing the word "error"
    """
    # TODO: Implement this function
    # Hint: Use open() to read the file and loop through the lines
    pass


# Task 2: Write a user-entered message to a file
def write_message_to_file():
    """
    Ask the user to enter a message and write it to a file named message.txt.
    """
    # TODO: Implement this function
    # Hint: Use input() to get the message and open() with write mode
    pass


# Task 3: Handle file not found exception
def read_file_safely(filename):
    """
    Try to read a file and handle the case where the file does not exist.
    
    Args:
        filename (str): The name of the file to read
        
    Returns:
        list or None: A list of lines from the file, or None if the file doesn't exist
    """
    # TODO: Implement this function
    # Hint: Use try/except to catch FileNotFoundError
    pass


# Helper function to create a sample input.txt file
def create_sample_input_file():
    """
    Create a sample input.txt file with some lines containing the word "error".
    """
    lines = [
        "This is a sample log file.",
        "Everything is working correctly.",
        "ERROR: System could not complete the operation.",
        "User logged in successfully.",
        "Warning: Disk space is running low.",
        "error: Failed to connect to the server.",
        "Process completed with no issues.",
        "Error: Invalid user credentials."
    ]
    
    try:
        with open("input.txt", "w") as file:
            for line in lines:
                file.write(line + "\n")
        print("Created sample input.txt file.")
    except Exception as e:
        print(f"Failed to create sample file: {e}")


# Main function to run all tasks
def main():
    # Create a sample input file for Task 1
    create_sample_input_file()
    
    print("\n=== Task 1: Count Error Lines ===\n")
    error_count = count_error_lines()
    print(f"Number of lines containing 'error': {error_count}")
    
    print("\n=== Task 2: Write Message to File ===\n")
    write_message_to_file()
    
    print("\n=== Task 3: Handle File Not Found ===\n")
    # Try to read an existing file
    print("Trying to read message.txt:")
    lines = read_file_safely("message.txt")
    if lines is not None:
        print(f"Successfully read {len(lines)} lines from message.txt")
    
    # Try to read a non-existent file
    print("\nTrying to read nonexistent.txt:")
    lines = read_file_safely("nonexistent.txt")
    if lines is None:
        print("Handled the case where the file doesn't exist.")


# Run the program
if __name__ == "__main__":
    main()
