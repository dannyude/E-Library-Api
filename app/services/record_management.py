from uuid import UUID, uuid4
from fastapi import HTTPException
from core.data import users_db, borrow_records_db


class RecordManagement:

    @staticmethod
    # endpoint to view borrowing records for a specific user.
    def borrowed_books_for_specific_user(user_id: UUID):
        user_id = str(user_id)

        user_records = []

        if user_id not in users_db:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        for record_id, record_data in borrow_records_db.items():

            if record_data["user_id"] == user_id:
                user_records.append(
                    {
                        "record_id": record_id,
                        "book_id": record_data["book_id"],
                        "borrow_date": record_data["borrow_date"],
                        "return_date": record_data["return_date"],
                    }
                )
        return user_records

    @staticmethod
    # Endpoint to view all borrowing records.
    def read_all_borrowing_records():
        all_records = []
        for record_id, record_data in borrow_records_db.items():
            all_records.append(
                {
                    "record_id": record_id,
                    "user_id": record_data["user_id"],
                    "book_id": record_data["book_id"],
                    "borrow_date": record_data["borrow_date"],
                    "return_date": record_data["return_date"],
                }
            )
        return {"message": "All records", "records": all_records}
