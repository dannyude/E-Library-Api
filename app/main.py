from fastapi import FastAPI
from api.v1.endpoints.users import user_router
from api.v1.endpoints.books import book_router
from api.v1.endpoints.book_operations import book_operations_router
from api.v1.endpoints.record_management import record_management_router


app = FastAPI()


app.include_router(user_router, tags=["Users"], prefix="/v1")


app.include_router(book_router, tags=["Books"], prefix="/v1")


app.include_router(book_operations_router, tags=["Book Operations"], prefix="/v1")

app.include_router(
    record_management_router, tags=["Record Management"], prefix="/private/v1"
)
