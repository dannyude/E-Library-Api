from typing import Annotated
from datetime import date
from uuid import UUID, uuid4
from fastapi import Body, HTTPException
from schemas.borrow_record import ReturnDate
from core.data import users_db, books, borrow_records_db


class BookOperations:
    @staticmethod
    # allows an active user to borrow an available book.

    def user_borrow(user_id: UUID, book_id: UUID):

        user_id = str(user_id)
        book_id = str(book_id)

        if user_id not in users_db:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        # Check if user is active
        if not users_db[user_id]["is_active"]:
            raise HTTPException(
                status_code=400,
                detail="User account is deactivated",
            )

        # check if books exists
        if book_id not in books:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )

        # check if book is available
        if not books[book_id]["is_available"]:
            raise HTTPException(
                status_code=400,
                detail="Book is unavailable",
            )

        # Create a new borrow record
        record_id = str(uuid4())
        borrow_records_db[record_id] = {
            "record_id": record_id,
            "user_id": user_id,
            "book_id": book_id,
            "borrow_date": date.today(),
            "return_date": None,
        }

        # Update the book's availability status
        books[book_id]["is_available"] = False

        return {"message": "Book has been borrowed successfully"}

    @staticmethod
    # Check if user has already borrowed the book
    def is_book_borrowed_by_the_same_user(user_id: UUID, book_id: UUID):

        user_id = str(user_id)
        book_id = str(book_id)

        if user_id not in users_db:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        for record_id, record_data in borrow_records_db.items():
            if (
                borrow_records_db[record_id]["user_id"] == user_id
                and borrow_records_db[record_id]["book_id"] == book_id
            ):
                raise HTTPException(
                    status_code=400,
                    detail="User has already borrowed this book",
                )
        # Check if book is available
        if not books[book_id]["is_available"]:
            raise HTTPException(
                status_code=400,
                detail="Book is unavailable",
            )

    @staticmethod
    # book is successfully borrowed, update it's is_available status to False.
    def update_book_availability(book_id: UUID):
        book_id = str(book_id)

        if book_id not in books:
            raise HTTPException(
                status_code=409,
                detail="Book is already borrowed by another user.",
            )

        # Update the book's availability status
        books[book_id]["is_available"] = False
        return {"message": "Book has been borrowed successfully"}

    @staticmethod
    # check if book cannot be borrowed, return an appropriate response and status code.
    def book_is_not_available(
        book_id: UUID,
    ):
        book_id = str(book_id)

        if book_id not in books:
            raise HTTPException(
                status_code=404,
                detail="Book not found or unavailable",
            )

        if not books[book_id]["is_available"]:
            raise HTTPException(
                status_code=400,
                detail="Book is not available",
            )

        return {"message": "Book is available"}

    @staticmethod
    # marks a borrowed book as returned by updating the return_date in the BorrowRecord and setting the book’s is_available status to True.
    def book_is_returned(
        record_id: UUID, return_record: Annotated[ReturnDate, Body(...)]
    ):
        record_id = str(record_id)
        if record_id not in borrow_records_db:
            raise HTTPException(
                status_code=404,
                detail="Record not found",
            )
        if return_record.date_returned is None:
            raise HTTPException(
                status_code=400,
                detail="Please enter the return date",
            )

        if return_record is not None:
            valid_date = return_record.date_returned
            borrow_records_db[record_id]["return_date"] = valid_date
            if valid_date < date.today():
                raise HTTPException(
                    status_code=400,
                    detail="Invalid date. Please enter a valid date.",
                )

        book_id = borrow_records_db[record_id]["book_id"]
        books[book_id]["is_available"] = True

        return {
            "message": "Book has been returned successfully",
            "return_record": borrow_records_db[record_id],
        }
