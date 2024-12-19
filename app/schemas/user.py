from pydantic import BaseModel, EmailStr
from uuid import UUID, uuid4


class CreateUser(BaseModel):
    username: str
    full_name: str
    email: EmailStr


class User(CreateUser):
    id: UUID = str(uuid4())
    is_active: bool = True


class UpdateUser(BaseModel):
    username: str | None = None
    full_name: str | None = None
    email: EmailStr | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    is_active: bool
    message: str
