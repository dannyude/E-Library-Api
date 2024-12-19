from typing import Annotated
from uuid import UUID, uuid4
from fastapi import Body, HTTPException
from core.data import users_db
from schemas.user import CreateUser, User, UpdateUser


# create a new user
class UserCrud:
    @staticmethod
    def create_user(
        user: Annotated[CreateUser, Body(...)],
        new_user_id: UUID = uuid4(),
    ):
        for _, users in users_db.items():
            if (
                users.get("email") == user.email
                or users.get("username") == user.username
            ):
                raise HTTPException(
                    status_code=400,
                    detail="Email or username already registered",
                )

        # Create new user entry
        new_user_id = uuid4()
        new_user = User(id=new_user_id, **user.model_dump())
        users_db[new_user_id] = new_user.model_dump()
        return {"user_id": new_user_id, "user": users_db[new_user_id]}

    # read all users
    @staticmethod
    def read_all_users():
        lst = []
        for user_id, user in users_db.items():
            lst.append({"user_id": user_id, "user": user})
        return lst

    # read a single user
    @staticmethod
    def read_user(user_id: UUID):
        user_id = str(user_id)
        if user_id not in users_db:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        return {"user_id": user_id, "user": users_db[user_id]}

    # update a user
    @staticmethod
    def update_user(
        user_id: UUID,
        user: Annotated[UpdateUser, Body(...)],
        exlude_unset=True,
    ):
        user_id = str(user_id)
        if user_id not in users_db:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        for key, value in user.model_dump(exclude_unset=exlude_unset).items():
            if value is not None:
                users_db[user_id][key] = value
        return {"user": users_db[user_id]}

    # deactivate a user
    @staticmethod
    def deactivate_user(user_id: UUID):
        user_id = str(user_id)
        if user_id not in users_db:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        users_db[user_id]["is_active"] = False
        return {
            "username": users_db[user_id].get("username"),
            "email": users_db[user_id].get("email"),
            "is_active": users_db[user_id]["is_active"],
            "message": "User deactivated successfully",
        }

    # delete a user
    @staticmethod
    def delete_user(user_id: UUID):
        user_id = str(user_id)
        if user_id not in users_db:
            raise HTTPException(
                status_code=404,
                detail="User not found",
            )
        del users_db[user_id]
        return {"message": "User deleted successfully"}

