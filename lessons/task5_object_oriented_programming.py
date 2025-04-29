#!/usr/bin/env python3

"""
Task 5: Object-Oriented Programming

This lesson covers:
- Creating classes and objects
- Class methods and attributes
- Inheritance

Complete the classes below according to the instructions.
"""

# Task 1: Create a class called Task with a name and a status
class Task:
    """
    A class representing a task with a name and status.
    
    Attributes:
        name (str): The name of the task
        status (str): The status of the task (default: "pending")
    
    Methods:
        mark_done(): Change the status to "done"
    """
    # TODO: Implement the class
    # Hint: Define __init__ method to initialize attributes and mark_done() method to change status
    pass


# Task 2: Create a class called ScraperTask that inherits from Task
class ScraperTask(Task):
    """
    A class representing a scraper task, inheriting from Task.
    
    Methods:
        run(): Print "Scraper running..."
    """
    # TODO: Implement the class
    # Hint: Use inheritance and define the run() method
    pass


# Main function to test the classes
def main():
    print("\n=== Task 1: Task Class ===\n")
    # Create a Task object
    task = Task("Complete Python assignment")
    print(f"Task name: {task.name}")
    print(f"Initial status: {task.status}")
    
    # Mark the task as done
    task.mark_done()
    print(f"Status after marking done: {task.status}")
    
    print("\n=== Task 2: ScraperTask Class ===\n")
    # Create a ScraperTask object
    scraper_task = ScraperTask("Scrape website data")
    print(f"ScraperTask name: {scraper_task.name}")
    print(f"Initial status: {scraper_task.status}")
    
    # Run the scraper task
    scraper_task.run()
    
    # Mark the scraper task as done
    scraper_task.mark_done()
    print(f"Status after marking done: {scraper_task.status}")


# Run the program
if __name__ == "__main__":
    main()
