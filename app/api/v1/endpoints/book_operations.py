from typing import Annotated
from fastapi import APIRouter, Body
from uuid import UUID, uuid4
from services.book_operations import BookOperations
from schemas.borrow_record import ReturnDate


book_operations_router = APIRouter()


# allows an active user to borrow an available book.
@book_operations_router.post("/users/{user_id}/borrow", status_code=201)
def user_borrow(user_id: UUID, book_id: UUID):
    return BookOperations.user_borrow(user_id, book_id)


# Check if user has already borrowed the book
@book_operations_router.post("/borrow/{user_id}/{book_id}")
def is_book_borrowed_by_the_same_user(user_id: UUID, book_id: UUID):
    return BookOperations.is_book_borrowed_by_the_same_user(user_id, book_id)


# Update the book's availability status to unavailable
@book_operations_router.put("/books/{book_id}/availability")
def update_book_availability(book_id: UUID):
    return BookOperations.update_book_availability(book_id)


# check if book cannot be borrowed, Update the book's availability status to unavailable
@book_operations_router.put("/books/{book_id}/status")
def book_is_not_available(
    book_id: UUID,
):
    return BookOperations.book_is_not_available(book_id)


# marks a borrowed book as returned by updating the return_date in the BorrowRecord
@book_operations_router.put("/users/return/{record_id}")
def book_is_returned(record_id: UUID, return_record: Annotated[ReturnDate, Body(...)]):

    return BookOperations.book_is_returned(record_id, return_record)
