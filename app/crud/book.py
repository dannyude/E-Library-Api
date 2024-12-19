from datetime import date
from typing import Annotated
from uuid import UUID, uuid4
from fastapi import Body, HTTPException
from core.data import books
from schemas.book import Book, BookOut, UpdateBook


class BookCrud:
    @staticmethod
    # create a new book
    def create_book(book: Annotated[Book, Body(...)], new_book_id: UUID = uuid4()):
        for _, existing_book in books.items():
            if existing_book.get("title") == book.title:
                raise HTTPException(
                    status_code=400,
                    detail="Book already exists",
                )
        new_book_id = uuid4()
        new_book = BookOut(id=new_book_id, **books)
        books[new_book_id] = new_book.model_dump()
        return {"message": "Book created successfully", "book": new_book}

    @staticmethod
    # get all books
    def read_all_books():

        all_books = []

        for book_id, book in books.items():
            all_books.append(BookOut(id=book_id, **book))
        return {"total_books": len(all_books), "books": all_books}

    @staticmethod
    # get a single book by id
    def read_book_by_id(book_id: UUID):

        book_id = str(book_id)

        if book_id not in books:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )
        return BookOut(id=book_id, **books[book_id])

    @staticmethod
    # update a book by id
    def update_book(book_id: UUID, Updated_book: Annotated[UpdateBook, Body(...)]):

        book_id = str(book_id)

        if book_id not in books:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )
        if book_id in books:
            for key, value in Updated_book.model_dump(exclude_unset=True).items():
                if value is not None:
                    books[book_id][key] = value
        return {"book": books[book_id]}

    @staticmethod
    # make a book unavailable
    def mark_book_unavailable(book_id: UUID):

        book_id = str(book_id)

        if book_id not in books:
            raise HTTPException(
                status_code=404,
                detail="Book not found or unavailable",
            )
        book_mark = books[book_id]["is_available"] = False
        return {
            "book_id": book_id,
            "title": books[book_id]["title"],
            "message": "Book has been marked as unavailable",
            "is_available": book_mark,
        }

    @staticmethod
    # delete a book by id
    def delete_book(book_id: UUID):

        book_id = str(book_id)

        if book_id not in books:
            raise HTTPException(
                status_code=404,
                detail="Book not found",
            )
        deleted_book = books[book_id]["title"]
        del books[book_id]
        return {"message": "Book deleted successfully", "deleted_book": deleted_book}
