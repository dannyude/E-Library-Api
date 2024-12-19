from unittest.mock import patch
import pytest
from fastapi import status
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


# Test borrowed books for a specific user
@patch("services.record_management.RecordManagement.borrowed_books_for_specific_user")
def test_borrowed_books_for_a_specific_user(
    mocked_function, users_mock_db, borrow_records_mock_db
):
    user_id = "dab19b42-565d-49e2-a43f-8a948360f52b"
    record_id = "d44f1d8c-905b-4ff6-8469-29acf1041897"

    mocked_function.return_value = [
        {
            "record_id": record_id,
            "book_id": borrow_records_mock_db[record_id]["book_id"],
            "borrow_date": borrow_records_mock_db[record_id]["borrow_date"],
            "return_date": borrow_records_mock_db[record_id]["return_date"],
        }
    ]

    response = client.get(f"/private/v1/users/{user_id}/borrowed_books")
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mocked_function.return_value


# Test borrowed books to view all borrowed books
@patch("services.record_management.RecordManagement.read_all_borrowing_records")
def test_borrowed_books_for_all_users(mocked_function, borrow_records_mock_db):

    mocked_function.return_value = [borrow_records_mock_db]

    response = client.get("/private/v1/borrowed_books")

    assert response.json() == mocked_function.return_value
    assert response.status_code == status.HTTP_200_OK
