from uuid import UUID, uuid4  # pylint: disable=unused-import
from fastapi import APIRouter
from services.record_management import RecordManagement

record_management_router = APIRouter()


# endpoint to view borrowing records for a specific user.
@record_management_router.get("/users/{user_id}/borrowed_books")
def borrowed_books_for_a_specific_user(user_id: UUID):
    return RecordManagement.borrowed_books_for_specific_user(user_id)


@record_management_router.get("/borrowed_books")
def borrowed_books_for_all_users():
    return RecordManagement.read_all_borrowing_records()
