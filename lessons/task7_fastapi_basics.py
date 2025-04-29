#!/usr/bin/env python3

"""
Task 7: FastAPI API Basics

This lesson covers:
- Creating a simple FastAPI application
- Defining GET and POST routes
- Testing API endpoints locally

Complete the functions below according to the instructions.
"""

"""
To complete this task, you need to have FastAPI installed.

Run the following command in your terminal to install FastAPI and Uvicorn:

pip install fastapi uvicorn

After implementing the code below, you can run the API with:

uvicorn task7_fastapi_basics:app --reload

Then you can access the API at http://localhost:8000
"""

# Task: Create a FastAPI app with GET and POST routes

# TODO: Import FastAPI and other necessary modules
# from fastapi import FastAPI, Body
# from pydantic import BaseModel

# TODO: Create a FastAPI instance
# app = FastAPI()

# TODO: Define a model for the request body of the POST route
# class TextRequest(BaseModel):
#     text: str

# TODO: Create a GET route at /hello that returns {"message": "Hello World"}
# @app.get("/hello")
# def hello_world():
#     pass

# TODO: Create a POST route at /echo that accepts a JSON body with text, and returns the same text back
# @app.post("/echo")
# def echo_text(request: TextRequest):
#     pass

"""
Testing the API:

1. Using curl for the GET route:
   curl http://localhost:8000/hello

2. Using curl for the POST route:
   curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello, FastAPI!"}' http://localhost:8000/echo

3. Using a browser:
   - Open http://localhost:8000/hello in your browser
   - For the POST route, you can use the automatic documentation at http://localhost:8000/docs
"""
