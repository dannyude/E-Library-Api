from unittest.mock import patch
from uuid import uuid4
import pytest
from fastapi import status
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


@pytest.fixture
def books_db():
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
    }


@patch("crud.book.BookCrud.create_book")
def test_create_book(mock_create_book):

    new_book_id = uuid4()

    mock_user = {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
    }
    mock_create_book.return_value = {
        "message": "Book created successfully",
        "book": {
            "id": str(new_book_id),
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "is_available": True,
        },
    }

    response = client.post("/v1/books", json=mock_user)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "message": "Book created successfully",
        "book": {
            "id": str(new_book_id),
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "is_available": True,
        },
    }


# Test read all books
@patch("crud.book.BookCrud.read_all_books")
def test_read_all_books(mock_read_all_books):
    mock_read_all_books.return_value = [
        {
            "id": str(uuid4()),
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "is_available": True,
        },
        {
            "id": str(uuid4()),
            "title": "The Da Vinci Code",
            "author": "Dan Brown",
            "is_available": False,
        },
        {
            "id": str(uuid4()),
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "is_available": True,
        },
    ]

    response = client.get("/v1/books")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mock_read_all_books.return_value


# Test read book by id
@patch("crud.book.BookCrud.read_book_by_id")
def test_read_book_by_id(mock_read_book_by_id):

    book_id = uuid4()

    mock_read_book_by_id.return_value = {
        "id": str(book_id),
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "is_available": True,
    }

    response = client.get(f"/v1/books/{book_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mock_read_book_by_id.return_value


# Test update book
@patch("crud.book.BookCrud.update_book")
def test_update_book(mock_update_book):

    book_id = uuid4()

    mock_update_book.return_value = {
        "book": {
            "id": str(book_id),
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "is_available": False,
        },
    }

    response = client.put(
        f"/v1/books/{book_id}",
        json={
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "is_available": False,
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mock_update_book.return_value


# Test mark book unavailable
@patch("crud.book.BookCrud.mark_book_unavailable")
def test_mark_book_unavailable(mock_mark_book_unavailable, books_db):

    book_id = "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d"

    books_db[book_id]["is_available"] = False

    mock_mark_book_unavailable.return_value = {
        "book_id": str(book_id),
        "title": "The Alchemist",
        "is_available": False,
    }

    response = client.patch(f"/v1/books/{book_id}/unavailable")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mock_mark_book_unavailable.return_value
    assert books_db[book_id]["is_available"] is False


# Test delete book
@patch("crud.book.BookCrud.delete_book")
def test_delete_book(mock_delete_book, books_db):

    book_id = "e5b6d127-8f90-4326-9358-f9d3b2ef3c5d"

    del books_db[book_id]

    mock_delete_book.return_value = {
        "message": "Book deleted successfully",
    }

    response = client.delete(f"/v1/books/{book_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mock_delete_book.return_value
    assert book_id not in books_db
