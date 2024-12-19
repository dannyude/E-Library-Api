from unittest.mock import patch
from uuid import UUID, uuid4
import pytest
from fastapi import status, HTTPException
from fastapi.testclient import TestClient


from main import app


client = TestClient(app)


@pytest.fixture
def users_mock_db():
    return {
        "dab19b42-565d-49e2-a43f-8a948360f52b": {
            "username": "Desayo",
            "full_name": "Desayo lol",
            "email": " desayo@gmail.com",
            "is_active": True,
        },
        "f0722861-4ba5-49a7-b16a-ff7b71373df5": {
            "username": "Chidi",
            "full_name": "Chidi tofu",
            "email": "chidi@gmail.com",
            "is_active": False,
        },
    }


@pytest.fixture
def books_mock_db():
    return {
        "7e8b4dfc-9a5a-4c2b-87bb-873cf9c6b2f3": {
            "title": "Heart stopper",
            "author": "Alice Oseman",
            "is_available": True,
        },
        "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d": {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "is_available": True,
        },
        "b0b0d128-9f31-4cfb-87af-ffbc1c1e5a9b": {
            "title": "Rich Dad Poor Dad",
            "author": "Robert Kiyosaki",
            "is_available": False,
        },
        "9a9e17e9-0d64-41e5-9fc3-7c2e3b2c7b98": {
            "title": "Everything is F*cked",
            "author": "Mark Manson",
            "is_available": False,
        },
    }


@pytest.fixture
def borrow_records_mock_db():
    return {
        "77998029-0050-47d4-9e7e-150ad428d7f0": {
            "user_id": "e8b0c7b3-2fbf-4a96-8f27-fd8e9e4c7d33",
            "book_id": "7e8b4dfc-9a5a-4c2b-87bb-873cf9c6b2f3",
            "borrow_date": "2024-10-01",
            "return_date": "2024-12-10",
        },
        "d44f1d8c-905b-4ff6-8469-29acf1041897": {
            "user_id": "dab19b42-565d-49e2-a43f-8a948360f52b",
            "book_id": "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d",
            "borrow_date": "2024-10-01",
            "return_date": "2024-12-10",
        },
    }


# Test for allowing an active user to borrow an available book
@patch("services.book_operations.BookOperations.user_borrow")
def test_user_borrow(mock_user_borrow):

    user_id = "81b075b3-f571-45de-aff0-3e667e8f6af4"
    book_id = "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d"

    mock_user_borrow.return_value = {"message": "Book has been borrowed successfully"}

    response = client.post(f"/v1/users/{user_id}/borrow?book_id={book_id}")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"message": "Book has been borrowed successfully"}


# Check if user has already borrowed the book
@patch("services.book_operations.BookOperations.is_book_borrowed_by_the_same_user")
def test_is_book_borrowed_by_the_same_user(mock_is_book_borrowed_by_the_same_user):

    user_id = UUID("81b075b3-f571-45de-aff0-3e667e8f6af4")
    book_id = UUID("e5b6d127-8f90-4326-9358-f9d3b2ef3c5d")

    # Test case 1: Book is already borrowed by the user
    mock_is_book_borrowed_by_the_same_user.side_effect = HTTPException(
        status_code=400, detail="User has already borrowed this book"
    )
    response = client.post(f"/v1/borrow/{user_id}/{book_id}")

    assert response.json() == {"detail": "User has already borrowed this book"}

    # Test case 2: Book is not borrowed by the user, and is not available
    mock_is_book_borrowed_by_the_same_user.reset_mock(side_effect=True)
    mock_is_book_borrowed_by_the_same_user.return_value = {
        "message": "book is not available"
    }

    response = client.post(f"/v1/borrow/{user_id}/{book_id}")

    assert response.json() == {"message": "book is not available"}


# If user is successful in borrowing a book, update the book's availability status to unavailable
@patch("services.book_operations.BookOperations.update_book_availability")
def test_user_borrow_success(mock_test_update_book_availability, books_mock_db):

    book_id = "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d"

    books_mock_db[book_id]["is_available"] = False

    mock_test_update_book_availability.return_value = {
        "message": "Book has been borrowed successfully"
    }

    response = client.put(f"/v1/books/{book_id}/availability")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Book has been borrowed successfully"}
    assert books_mock_db[book_id]["is_available"] is False


# If book cannot be borrowed, return an appropriate response and status code
@patch("services.book_operations.BookOperations.book_is_not_available")
def test_book_is_not_available(mock_book_is_not_available, books_mock_db):

    book_id = "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d"

    books_mock_db[book_id]["is_available"] = False

    mock_book_is_not_available.return_value = {"message": "Book is not available"}

    response = client.put(f"/v1/books/{book_id}/status")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "Book is not available"}
    assert books_mock_db[book_id]["is_available"] is False


# marks a borrowed book as returned by updating the return_date in the BorrowRecord
@patch("services.book_operations.BookOperations.book_is_returned")
def test_book_is_returned(mock_book_is_returned, borrow_records_mock_db):

    record_id = "77998029-0050-47d4-9e7e-150ad428d7f0"

    borrow_records_mock_db[record_id]["return_date"] = "2024-12-10"

    mock_data = {
        "date_returned": "2024-12-10",
    }

    mock_book_is_returned.return_value = {
        "message": "Book has been returned successfully",
        "record_id": record_id,
        "borrow_record": borrow_records_mock_db[record_id],
    }

    response = client.put(f"/v1/users/return/{record_id}", json=mock_data)
    assert response.json() == mock_book_is_returned.return_value
