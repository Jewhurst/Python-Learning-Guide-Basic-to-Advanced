#!/usr/bin/env python3

"""
Task 9: Database Integration with SQLAlchemy and PostgreSQL

This lesson covers:
- Setting up SQLAlchemy with PostgreSQL
- Defining database models
- Performing database operations (create, insert, query)

Complete the functions below according to the instructions.
"""

"""
To complete this task, you need to have SQLAlchemy, psycopg2, and alembic installed.

Run the following command in your terminal:

pip install sqlalchemy psycopg2-binary alembic

You'll also need a PostgreSQL database. You can:
1. Install PostgreSQL locally (https://www.postgresql.org/download/)
2. Use a Docker container
3. Use a free cloud service like ElephantSQL (https://www.elephantsql.com/)

Once you have a PostgreSQL database, update the DATABASE_URL below with your connection string.
"""

# TODO: Import necessary modules
# from sqlalchemy import create_engine, Column, Integer, String, DateTime, inspect
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from datetime import datetime

# TODO: Set up database connection
# Replace this with your actual PostgreSQL connection string
# DATABASE_URL = "postgresql://username:password@localhost:5432/dbname"
# engine = create_engine(DATABASE_URL)
# Base = declarative_base()
# Session = sessionmaker(bind=engine)

# TODO: Define the User model
# class User(Base):
#     """User model with id, email, and created_at fields."""
#     __tablename__ = 'users'
#     
#     # Define columns here
#     # id = Column(...)
#     # email = Column(...)
#     # created_at = Column(...)
#     
#     def __repr__(self):
#         """String representation of the User object."""
#         return f"<User(id={self.id}, email='{self.email}', created_at={self.created_at})>"

# TODO: Create tables in the database
def create_tables():
    """
    Create the tables in the database based on the defined models.
    """
    # Base.metadata.create_all(engine)
    pass

# TODO: Insert a new user
def insert_user(email):
    """
    Insert a new user with the given email into the database.
    
    Args:
        email (str): The email of the user to insert
        
    Returns:
        User: The newly created User object
    """
    # session = Session()
    # try:
    #     # Create a new user
    #     # Add to session
    #     # Commit the session
    #     # Return the user
    #     pass
    # except Exception as e:
    #     # Handle exceptions
    #     # Rollback the session
    #     pass
    # finally:
    #     # Close the session
    #     pass
    pass

# TODO: Query all users
def query_users():
    """
    Query all users from the database and print their emails.
    
    Returns:
        list: A list of all User objects
    """
    # session = Session()
    # try:
    #     # Query all users
    #     # Print each user's email
    #     # Return the list of users
    #     pass
    # except Exception as e:
    #     # Handle exceptions
    #     pass
    # finally:
    #     # Close the session
    #     pass
    pass

# Main function to run all tasks
def main():
    print("\n=== Task 1: Create Tables ===\n")
    create_tables()
    print("Tables created successfully!")
    
    print("\n=== Task 2: Insert Users ===\n")
    # Insert some sample users
    insert_user("user1@example.com")
    insert_user("user2@example.com")
    insert_user("user3@example.com")
    
    print("\n=== Task 3: Query Users ===\n")
    users = query_users()
    print(f"Total users: {len(users)}")

# Run the program
if __name__ == "__main__":
    main()
