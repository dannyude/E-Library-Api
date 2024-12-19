from typing import Optional
from datetime import date
from pydantic import BaseModel
from uuid import UUID, uuid4


class BorrowRecord(BaseModel):
    user_id: UUID
    book_id: UUID
    borrow_date: date
    return_date: Optional[date] = None


class ReturnRecord(BaseModel):
    record_id: UUID
    user_id: UUID
    book_id: UUID
    return_date: date | None = None


class ReturnDate(BaseModel):
    date_returned: date | None = None
