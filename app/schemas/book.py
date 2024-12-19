from pydantic import BaseModel
from uuid import UUID, uuid4


class Book(BaseModel):
    title: str
    author: str


class BookOut(BaseModel):
    id: UUID
    title: str
    author: str
    is_available: bool = True


class book_available(Book):
    id: UUID
    is_available: bool = True


class UpdateBook(BaseModel):
    title: str | None = None
    author: str | None = None
