#!/usr/bin/env python3

"""
Task 10: Async Programming and HTTP Requests (SOLUTION)

This lesson covers:
- Asynchronous programming with asyncio
- Making HTTP requests with httpx or aiohttp
- Measuring response times
- Concurrent API calls

Complete implementation of all functions.
"""

"""
To run this code, you need to have httpx installed.

Run the following command in your terminal:

pip install httpx

This example uses httpx, but you could also use aiohttp with similar patterns.
"""

# Import necessary modules
import asyncio
import httpx
import time
from typing import List, Dict, Any

# List of APIs to fetch data from
APIs = [
    "https://jsonplaceholder.typicode.com/posts/1",  # Fake blog post
    "https://jsonplaceholder.typicode.com/users/1",   # Fake user
    "https://jsonplaceholder.typicode.com/todos/1"    # Fake todo
]

# Fetch data from a single API
async def fetch_data(client: httpx.AsyncClient, url: str) -> Dict[str, Any]:
    """
    Fetch data from a single API and measure the response time.
    
    Args:
        client: The httpx AsyncClient to use for the request
        url: The URL to fetch data from
        
    Returns:
        A dictionary containing the response data, status code, and response time
    """
    # Record the start time
    start_time = time.time()
    
    try:
        # Make the request
        response = await client.get(url)
        
        # Record the end time
        end_time = time.time()
        
        # Calculate the response time in milliseconds
        response_time_ms = (end_time - start_time) * 1000
        
        # Return a dictionary with the results
        return {
            "url": url,
            "status_code": response.status_code,
            "response_time_ms": round(response_time_ms, 2),
            "data": response.json() if response.status_code == 200 else None
        }
    
    except Exception as e:
        # Record the end time even if there's an error
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000
        
        # Return a dictionary with error information
        return {
            "url": url,
            "status_code": None,
            "response_time_ms": round(response_time_ms, 2),
            "error": str(e),
            "data": None
        }

# Fetch data from multiple APIs concurrently
async def fetch_all_data(urls: List[str]) -> List[Dict[str, Any]]:
    """
    Fetch data from multiple APIs concurrently using asyncio.gather().
    
    Args:
        urls: A list of URLs to fetch data from
        
    Returns:
        A list of dictionaries containing the response data, status code, and response time for each URL
    """
    # Create an async client
    async with httpx.AsyncClient() as client:
        # Use asyncio.gather to fetch data from all URLs concurrently
        tasks = [fetch_data(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        return results

# Run the async functions
async def main_async():
    """
    Main async function to run the async code.
    """
    print("Fetching data from multiple APIs concurrently...")
    
    # Start timing the entire operation
    total_start_time = time.time()
    
    # Call fetch_all_data with the list of APIs
    results = await fetch_all_data(APIs)
    
    # Calculate total time
    total_time_ms = (time.time() - total_start_time) * 1000
    
    # Print the results
    print(f"\nResults (total time: {round(total_time_ms, 2)}ms):")
    for result in results:
        if "error" in result and result["error"]:
            print(f"URL: {result['url']}")
            print(f"Error: {result['error']}")
            print(f"Response time: {result['response_time_ms']}ms")
        else:
            print(f"URL: {result['url']}")
            print(f"Status code: {result['status_code']}")
            print(f"Response time: {result['response_time_ms']}ms")
            print(f"Data: {result['data']}")
        print()
    
    # Compare with sequential execution
    print("\nComparing with sequential execution:")
    await sequential_comparison(APIs)

# Sequential comparison for demonstration
async def sequential_comparison(urls: List[str]):
    """
    Fetch the same data sequentially for comparison.
    
    Args:
        urls: A list of URLs to fetch data from
    """
    # Start timing the entire operation
    total_start_time = time.time()
    
    # Create an async client
    async with httpx.AsyncClient() as client:
        # Fetch each URL one at a time
        results = []
        for url in urls:
            result = await fetch_data(client, url)
            results.append(result)
    
    # Calculate total time
    total_time_ms = (time.time() - total_start_time) * 1000
    
    # Print the total time for comparison
    print(f"Sequential execution total time: {round(total_time_ms, 2)}ms")
    
    # Calculate and print the difference
    concurrent_time = sum(result["response_time_ms"] for result in results)
    sequential_time = total_time_ms
    time_saved = sequential_time - concurrent_time
    
    print(f"Time saved with concurrent execution: {round(time_saved, 2)}ms")
    print(f"Efficiency improvement: {round((time_saved / sequential_time) * 100, 2)}%")

# Main function to run all tasks
def main():
    print("\n=== Task: Async HTTP Requests ===\n")
    
    # Run the async function
    asyncio.run(main_async())
    
    print("\nAll requests completed!")

# Run the program
if __name__ == "__main__":
    main()
