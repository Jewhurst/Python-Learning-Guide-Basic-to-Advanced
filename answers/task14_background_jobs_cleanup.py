#!/usr/bin/env python3

"""
Task 14: Background Jobs and Cleanup Automation (SOLUTION)

This lesson covers:
- Scheduling recurring jobs with the schedule library
- File operations for cleanup tasks
- Logging with timestamps

Complete implementation of all functions.
"""

"""
To run this code, you need to have the schedule library installed.

Run the following command in your terminal:

pip install schedule
"""

# Import necessary modules
import schedule
import time
import os
import logging
from datetime import datetime, timedelta
import glob

# Set up logging
def setup_logging():
    """Configure logging with timestamps."""
    # Configure logging with a specific format
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    return logging.getLogger(__name__)

# Create a function to delete old log files
def cleanup_old_logs(directory, hours=1):
    """Delete .log files older than the specified number of hours.
    
    Args:
        directory (str): Directory containing log files
        hours (int): Number of hours to keep files for
        
    Returns:
        int: Number of files deleted
    """
    # Calculate the cutoff time
    cutoff_time = datetime.now() - timedelta(hours=hours)
    logger.info(f"Deleting .log files older than {cutoff_time}")
    
    # Find all .log files in the directory
    log_files = glob.glob(os.path.join(directory, "*.log"))
    logger.info(f"Found {len(log_files)} .log files in {directory}")
    
    # Track deleted files
    deleted_count = 0
    
    # Check each file's modification time
    for log_file in log_files:
        # Get the file's modification time
        mod_time = datetime.fromtimestamp(os.path.getmtime(log_file))
        
        # Delete files older than the cutoff time
        if mod_time < cutoff_time:
            try:
                os.remove(log_file)
                logger.info(f"Deleted old log file: {log_file} (modified: {mod_time})")
                deleted_count += 1
            except Exception as e:
                logger.error(f"Error deleting {log_file}: {e}")
    
    # Log the results
    logger.info(f"Cleanup complete. Deleted {deleted_count} old log files.")
    return deleted_count

# Create a function to create sample log files for testing
def create_sample_logs(directory, count=5):
    """Create sample log files for testing the cleanup function.
    
    Args:
        directory (str): Directory to create log files in
        count (int): Number of log files to create
        
    Returns:
        list: Paths of created log files
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
        logger.info(f"Created directory: {directory}")
    
    created_files = []
    
    # Create sample log files with timestamps
    for i in range(count):
        # Create a timestamp with some files older than 1 hour
        if i < count // 2:
            # Create older files (2 hours ago)
            timestamp = datetime.now() - timedelta(hours=2)
        else:
            # Create newer files (30 minutes ago)
            timestamp = datetime.now() - timedelta(minutes=30)
        
        # Format the timestamp for the filename
        timestamp_str = timestamp.strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(directory, f"sample_log_{timestamp_str}_{i}.log")
        
        # Create the file with some content
        with open(filename, 'w') as f:
            f.write(f"This is a sample log file created at {timestamp}\n")
            f.write(f"It contains some sample log entries for testing.\n")
            f.write(f"Log entry 1: INFO - Application started\n")
            f.write(f"Log entry 2: DEBUG - Configuration loaded\n")
            f.write(f"Log entry 3: ERROR - Failed to connect to database\n")
        
        # Set the file's modification time to match the timestamp
        os.utime(filename, (timestamp.timestamp(), timestamp.timestamp()))
        
        created_files.append(filename)
        logger.info(f"Created sample log file: {filename} (timestamp: {timestamp})")
    
    logger.info(f"Created {len(created_files)} sample log files in {directory}")
    return created_files

# Create a function to run the scheduled job
def run_scheduled_job():
    """Run the cleanup job and log the execution."""
    # Log the job start time
    start_time = datetime.now()
    logger.info(f"Starting scheduled cleanup job at {start_time}")
    
    # Run the cleanup function
    deleted_count = cleanup_old_logs(log_directory)
    
    # Log the job completion
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    logger.info(f"Completed scheduled cleanup job at {end_time} (duration: {duration:.2f} seconds)")
    logger.info(f"Deleted {deleted_count} old log files")
    
    # Return a summary
    return {
        "start_time": start_time,
        "end_time": end_time,
        "duration": duration,
        "deleted_count": deleted_count
    }

# Main function to run all tasks
def main():
    print("\n=== Task: Background Jobs and Cleanup Automation ===\n")
    
    # Set up logging
    global logger
    logger = setup_logging()
    
    # Define the directory for log files
    global log_directory
    log_directory = "./temp_logs"
    
    # Create sample log files
    create_sample_logs(log_directory)
    
    # Schedule the cleanup job to run every 5 seconds
    schedule.every(5).seconds.do(run_scheduled_job)
    
    # Run the scheduled job loop
    print("Running scheduled cleanup job every 5 seconds. Press Ctrl+C to stop.")
    try:
        # Run the job immediately once
        run_scheduled_job()
        
        # Then run according to schedule
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduled job stopped.")
    
    print("\nTask completed!")

# Run the program
if __name__ == "__main__":
    main()
