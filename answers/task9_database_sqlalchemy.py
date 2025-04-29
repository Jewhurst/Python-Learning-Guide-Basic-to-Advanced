#!/usr/bin/env python3

"""
Task 9: Database Integration with SQLAlchemy and PostgreSQL (SOLUTION)

This lesson covers:
- Setting up SQLAlchemy with PostgreSQL
- Defining database models
- Performing database operations (create, insert, query)

Complete implementation of all functions.
"""

"""
To run this code, you need to have SQLAlchemy, psycopg2, and alembic installed.

Run the following command in your terminal:

pip install sqlalchemy psycopg2-binary alembic

You'll also need a PostgreSQL database. You can:
1. Install PostgreSQL locally (https://www.postgresql.org/download/)
2. Use a Docker container
3. Use a free cloud service like ElephantSQL (https://www.elephantsql.com/)

Once you have a PostgreSQL database, update the DATABASE_URL below with your connection string.
"""

# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, DateTime, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Set up database connection
# Replace this with your actual PostgreSQL connection string
# You can also use an environment variable for better security
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/postgres"
)

# Create engine and session
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the User model
class User(Base):
    """User model with id, email, and created_at fields."""
    __tablename__ = 'users'
    
    # Define columns
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        """String representation of the User object."""
        return f"<User(id={self.id}, email='{self.email}', created_at={self.created_at})>"

# Create tables in the database
def create_tables():
    """
    Create the tables in the database based on the defined models.
    First checks if the table already exists to avoid errors.
    """
    # Check if the table already exists
    inspector = inspect(engine)
    if 'users' not in inspector.get_table_names():
        Base.metadata.create_all(engine)
        print("Created 'users' table.")
    else:
        print("Table 'users' already exists.")

# Insert a new user
def insert_user(email):
    """
    Insert a new user with the given email into the database.
    
    Args:
        email (str): The email of the user to insert
        
    Returns:
        User: The newly created User object, or None if an error occurred
    """
    session = Session()
    try:
        # Check if user with this email already exists
        existing_user = session.query(User).filter(User.email == email).first()
        if existing_user:
            print(f"User with email '{email}' already exists.")
            return existing_user
        
        # Create a new user
        new_user = User(email=email)
        
        # Add to session and commit
        session.add(new_user)
        session.commit()
        
        print(f"Created new user with email: {email}")
        return new_user
    
    except Exception as e:
        # Handle exceptions
        print(f"Error inserting user: {e}")
        session.rollback()
        return None
    
    finally:
        # Close the session
        session.close()

# Query all users
def query_users():
    """
    Query all users from the database and print their emails.
    
    Returns:
        list: A list of all User objects
    """
    session = Session()
    try:
        # Query all users
        users = session.query(User).all()
        
        # Print each user's email
        print("User emails:")
        for user in users:
            print(f"- {user.email} (created at: {user.created_at})")
        
        return users
    
    except Exception as e:
        # Handle exceptions
        print(f"Error querying users: {e}")
        return []
    
    finally:
        # Close the session
        session.close()

# Additional function: Delete a user
def delete_user(email):
    """
    Delete a user with the given email from the database.
    
    Args:
        email (str): The email of the user to delete
        
    Returns:
        bool: True if the user was deleted, False otherwise
    """
    session = Session()
    try:
        # Find the user
        user = session.query(User).filter(User.email == email).first()
        
        if user:
            # Delete the user
            session.delete(user)
            session.commit()
            print(f"Deleted user with email: {email}")
            return True
        else:
            print(f"User with email '{email}' not found.")
            return False
    
    except Exception as e:
        # Handle exceptions
        print(f"Error deleting user: {e}")
        session.rollback()
        return False
    
    finally:
        # Close the session
        session.close()

# Main function to run all tasks
def main():
    print("\n=== Task 1: Create Tables ===\n")
    create_tables()
    
    print("\n=== Task 2: Insert Users ===\n")
    # Insert some sample users
    insert_user("user1@example.com")
    insert_user("user2@example.com")
    insert_user("user3@example.com")
    
    print("\n=== Task 3: Query Users ===\n")
    users = query_users()
    print(f"Total users: {len(users)}")
    
    print("\n=== Bonus: Delete a User ===\n")
    delete_user("user2@example.com")
    
    print("\n=== Query Users After Deletion ===\n")
    users = query_users()
    print(f"Total users after deletion: {len(users)}")

# Run the program
if __name__ == "__main__":
    main()
