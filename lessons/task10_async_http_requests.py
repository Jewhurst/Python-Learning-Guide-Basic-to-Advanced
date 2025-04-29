#!/usr/bin/env python3

"""
Task 10: Async Programming and HTTP Requests

This lesson covers:
- Asynchronous programming with asyncio
- Making HTTP requests with httpx or aiohttp
- Measuring response times
- Concurrent API calls

Complete the functions below according to the instructions.
"""

"""
To complete this task, you need to have httpx or aiohttp installed.

Run one of the following commands in your terminal:

pip install httpx
# OR
pip install aiohttp

This example will use httpx, but you can modify it to use aiohttp if you prefer.
"""

# TODO: Import necessary modules
# import asyncio
# import httpx
# import time
# from typing import List, Dict, Any

# List of APIs to fetch data from
APIs = [
    "https://jsonplaceholder.typicode.com/posts/1",  # Fake blog post
    "https://jsonplaceholder.typicode.com/users/1",   # Fake user
    "https://jsonplaceholder.typicode.com/todos/1"    # Fake todo
]

# TODO: Fetch data from a single API
# async def fetch_data(client: httpx.AsyncClient, url: str) -> Dict[str, Any]:
#     """
#     Fetch data from a single API and measure the response time.
#     
#     Args:
#         client: The httpx AsyncClient to use for the request
#         url: The URL to fetch data from
#         
#     Returns:
#         A dictionary containing the response data, status code, and response time
#     """
#     # Record the start time
#     # Make the request
#     # Record the end time
#     # Calculate the response time
#     # Return a dictionary with the results
#     pass

# TODO: Fetch data from multiple APIs concurrently
# async def fetch_all_data(urls: List[str]) -> List[Dict[str, Any]]:
#     """
#     Fetch data from multiple APIs concurrently using asyncio.gather().
#     
#     Args:
#         urls: A list of URLs to fetch data from
#         
#     Returns:
#         A list of dictionaries containing the response data, status code, and response time for each URL
#     """
#     # Create an async client
#     # Use asyncio.gather to fetch data from all URLs concurrently
#     # Return the results
#     pass

# TODO: Run the async functions
# async def main_async():
#     """
#     Main async function to run the async code.
#     """
#     # Print a message
#     # Call fetch_all_data with the list of APIs
#     # Print the results
#     pass

# Main function to run all tasks
def main():
    print("\n=== Task: Async HTTP Requests ===\n")
    
    # TODO: Run the async function
    # asyncio.run(main_async())
    
    print("\nAll requests completed!")

# Run the program
if __name__ == "__main__":
    main()
