# E-Library API System

## Description

The **E-Library API System** is a backend service for managing an online library. It provides endpoints to manage users, books, and borrowing operations, allowing users to borrow and return books while keeping track of book availability and user activity.

This project is built with **FastAPI** and uses **in-memory data structures** for storage, making it lightweight and easy to set up.

## Features

**User Management**:

- Create, read, update, and delete users.
- Deactivate user accounts.
- User login and password management.
- User status validation.

**Book Management**:

- Create, read, update, and delete books.
- Mark books as unavailable for borrowing.
- Validate book availability.

**Borrowing Operations**:

- Borrow available books if the user is active.
- Return borrowed books and update their availability.
- Prevent duplicate borrowing of the same book by the same user.

**Borrow Record Management**:

- View all borrowing records.
- View borrowing records for a specific user.

## Tech Stack

- **Framework:** FastAPI
- **Language:** Python
- **Data Storage:** In-memory structures (dictionaries)
- **Testing:** pytest

## Installation

- **Prerequisites:**
    - Python 3.9 or higher
    - `pip` package manager
- **Steps:**
    1. **Clone the repository:**

       ```bash
       git clone [https://github.com/dannyude/E-library-Api.git](https://github.com/dannyude/E-library-Api.git)
       ```

    2. **Create a virtual environment:**

       ```bash
       python -m venv venv
       source venv/bin/activate  # On Linux/macOS
       ```

       ```bash
       python -m venv venv
       source venv/Scripts/activate  # On Windows
       ```

    3. **Install dependencies:**

       ```bash
       pip install -r requirements.txt
       ```

    4. **Run the FastAPI server:**

       ```bash
       uvicorn main:app --reload
       ```

    5. **Open the API documentation in your browser:**

       - Swagger UI: http://127.0.0.1:8000/docs
       - Redoc: http://127.0.0.1:8000/redoc

## Project Structure

```
e-library-api

Alt Exams/
├── api/
│   ├── v1/  # For versioning your API
│   │   ├── endpoints/  
│   │   │   ├── __init__.py
│   │   │   ├── users.py
│   │   │   ├── books.py
│   │   │   |── book_operations.py 
|   |   |   |__ record_managem
│   │   
│   └── __init__.py
|
├── core/  # Core application logic and settings
│   ├── __init__.py
│   ├── data.py.py 
│   
├── crud/  # Database interaction logic (CRUD operations)
│   ├── __init__.py
│   ├── users.py
│   ├── books.py
│   
├── models/  # Database models (null)
│   ├── __init__.py
│  
├── schemas/  # Pydantic schemas for data validation
│   ├── __init__.py
│   ├── user.py
│   ├── book.py
│   └── borrow_record.py
├── services/  # Business logic and service layer
│   ├── __init__.py
│   ├── book_operations.py
│   ├── record_management.py
│   
├── tests/  # Test cases
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_books.py
│   |── test_record_management.py
|   |__ test_book_management.py
|
├── main.py  # Main application file
└── requirements.txt  # Project dependencies
Explanation

api/: This directory contains the API-related code, organized by version (v1/ in this case).

endpoints/: Holds the files where the API endpoints using FastAPI was defined.

api.py: The main API router that combines the endpoints from different modules.

core/: Contains core application logic, such as configuration settings and our in memeory database.

crud/: Holds the CRUD (Create, Read, Update, Delete) operations for interacting with our data storage.

models/: Holds our in memory database.

schemas/: Contains Pydantic schemas for data validation and serialization.

services/: This is where you implement your business logic and service layer, which orchestrates the interaction between API endpoints, CRUD operations, and other components.

tests/: Holds your test cases, organized by module or functionality.

main.py: The main application file that sets up and runs your FastAPI application.

requirements.txt: Lists the project's dependencies, which can be installed using pip install -r requirements.txt.
```