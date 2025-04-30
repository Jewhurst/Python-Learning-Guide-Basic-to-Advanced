#!/usr/bin/env python3

"""
Task 14: Background Jobs and Cleanup Automation

This lesson covers:
- Scheduling recurring jobs with the schedule library
- File operations for cleanup tasks
- Logging with timestamps

Complete the functions below according to the instructions.
"""

"""
To complete this task, you need to have the schedule library installed.

Run the following command in your terminal:

pip install schedule
"""

# TODO: Import necessary modules
# import schedule
# import time
# import os
# import logging
# from datetime import datetime, timedelta
# import glob

# TODO: Set up logging
# def setup_logging():
#     """Configure logging with timestamps."""
#     # Configure logging with a specific format
#     pass

# TODO: Create a function to delete old log files
# def cleanup_old_logs(directory, hours=1):
#     """Delete .log files older than the specified number of hours."""
#     # Calculate the cutoff time
#     # Find all .log files in the directory
#     # Check each file's modification time
#     # Delete files older than the cutoff time
#     # Log the results
#     pass

# TODO: Create a function to create sample log files for testing
# def create_sample_logs(directory, count=5):
#     """Create sample log files for testing the cleanup function."""
#     # Create the directory if it doesn't exist
#     # Create sample log files with timestamps
#     # Log the creation
#     pass

# TODO: Create a function to run the scheduled job
# def run_scheduled_job():
#     """Run the cleanup job and log the execution."""
#     # Log the job start time
#     # Run the cleanup function
#     # Log the job completion
#     pass

# Main function to run all tasks
def main():
    print("\n=== Task: Background Jobs and Cleanup Automation ===\n")
    
    # TODO: Set up logging
    # setup_logging()
    
    # TODO: Define the directory for log files
    # log_directory = "./temp_logs"
    
    # TODO: Create sample log files
    # create_sample_logs(log_directory)
    
    # TODO: Schedule the cleanup job to run every 5 seconds
    # schedule.every(5).seconds.do(run_scheduled_job)
    
    # TODO: Run the scheduled job loop
    # print("Running scheduled cleanup job every 5 seconds. Press Ctrl+C to stop.")
    # try:
    #     while True:
    #         schedule.run_pending()
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     print("\nScheduled job stopped.")
    
    print("\nTask completed!")

# Run the program
if __name__ == "__main__":
    main()
