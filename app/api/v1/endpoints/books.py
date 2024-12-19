from typing import Annotated
from fastapi import APIRouter, Body
from uuid import UUID, uuid4
from schemas.book import Book, UpdateBook
from crud.book import BookCrud


book_router = APIRouter()


# create a new book
@book_router.post("/books", status_code=201)
def create_book(book: Annotated[Book, Body(...)]):
    new_book = BookCrud.create_book(book)
    return new_book


# get all books
@book_router.get("/books")
def read_all_books():
    return BookCrud.read_all_books()


# get a single book by id
@book_router.get("/books/{book_id}")
def read_book_by_id(book_id: UUID):
    return BookCrud.read_book_by_id(book_id)


# update a book by id
@book_router.put("/books/{book_id}")
def update_book(book_id: UUID, updated_book: Annotated[UpdateBook, Body(...)]):
    return BookCrud.update_book(book_id, updated_book)


# make a book unavailable
@book_router.patch("/books/{book_id}/unavailable")
def mark_book_unavailable(book_id: UUID):
    return BookCrud.mark_book_unavailable(book_id)


# delete a book by id
@book_router.delete("/books/{book_id}")
def delete_book(book_id: UUID):
    return BookCrud.delete_book(book_id)
