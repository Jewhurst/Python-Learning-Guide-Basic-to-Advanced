# Python Onboarding Project

This project contains a series of Python lessons designed for onboarding and training new hires. Each lesson focuses on specific Python concepts and includes practical tasks to reinforce learning.

## Project Structure

- `lessons/`: Contains skeleton code files with basic structure and hints for each task
- `answers/`: Contains complete solutions for reference
- `tests/`: Contains test files for testing the implementations

## How to Use

1. Start with the files in the `lessons/` directory
2. Try to complete the tasks based on the provided instructions and skeleton code
3. If you get stuck, refer to the corresponding solution in the `answers/` directory

## Lessons

### Task 1: Basic Syntax, Strings, and Lists
- Concepts: input(), print(), list operations, string splitting, sorting
- File: `task1_basics.py`
- Tasks: Create a greeting script, print website URLs, sort comma-separated tags

### Task 2: Loops, Conditionals, and Functions
- Concepts: for loops, if/else, function definition, input validation logic
- File: `task2_functions_conditionals_loops.py`
- Tasks: Check if a number is even, print numbers (skipping divisible by 3), validate passwords

### Task 3: Dictionaries, Sets, Tuples
- Concepts: key-value access, deduplication, understanding immutable vs mutable data types
- File: `task3_dictionaries_sets_tuples.py`
- Tasks: Create a user dictionary, find unique emails, use tuples for user info

### Task 4: File I/O and Error Handling
- Concepts: open(), readlines(), exception handling with try/except
- File: `task4_file_io_error_handling.py`
- Tasks: Count error lines in a file, write user messages to a file, handle file not found errors

### Task 5: Object-Oriented Programming
- Concepts: OOP syntax, inheritance, basic class methods
- File: `task5_object_oriented_programming.py`
- Tasks: Create Task class, implement inheritance with ScraperTask

### Task 6: Packages and Environment Setup
- Concepts: virtual environments, package management, environment variables
- File: `task6_packages_environment.py`
- Tasks: Set up a virtual environment, install packages, use python-dotenv

### Task 7: FastAPI API Basics
- Concepts: FastAPI syntax, GET/POST basics, testing locally
- File: `task7_fastapi_basics.py`
- Tasks: Create a FastAPI app with hello and echo endpoints

### Task 8: Logging and Testing
- Concepts: testing real endpoints, basic API test coverage, structured logs
- File: `task8_logging_testing.py`
- Tasks: Add logging to a FastAPI app, write tests with pytest

### Task 9: Database Integration with SQLAlchemy and PostgreSQL
- Concepts: database connection, models, inserts, queries
- File: `task9_database_sqlalchemy.py`
- Tasks: Set up a PostgreSQL database, define a User model, perform CRUD operations

### Task 10: Async Programming and HTTP Requests
- Concepts: async flow, I/O performance, concurrency with real endpoints
- File: `task10_async_http_requests.py`
- Tasks: Use async programming to fetch data from multiple APIs concurrently

### Task 11: Auth and Pagination in FastAPI
- Concepts: FastAPI dependencies, security headers, basic access control, pagination logic
- File: `task11_fastapi_auth_pagination.py`
- Tasks: Implement authentication and pagination in a FastAPI app

### Task 12: Mocking and GitHub Actions
- Concepts: testing practice, CI setup, mocking external services
- File: `task12_mocking_github_actions.py`
- Tasks: Write tests that mock API calls and set up GitHub Actions for CI

### Task 13: Playwright Web Scraping with Error Handling
- Concepts: scraping automation, retry pattern, structured output
- File: `task13_playwright_web_scraping.py`
- Tasks: Set up Playwright, scrape a website with retry logic, save results to JSON

### Task 14: Background Jobs and Cleanup Automation
- Concepts: background work, scheduling, file operations, automation
- File: `task14_background_jobs_cleanup.py`
- Tasks: Use schedule to run a cleanup job, delete old log files, implement a job loop

### Task 15: Secure Config and Secrets Management
- Concepts: secure handling, simple encryption, config practice
- File: `task15_secure_config_secrets.py`
- Tasks: Load config from .env, encrypt/decrypt strings, validate email addresses

### Task 16: Full App Project
- Concepts: full-stack integration, FastAPI, scraping, database, background jobs, testing, CI
- File: `task16_full_app_project.py`
- Tasks: Build a complete web app that scrapes URLs, stores data in PostgreSQL, and includes background cleanup jobs

