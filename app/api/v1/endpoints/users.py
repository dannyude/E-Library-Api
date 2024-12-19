from fastapi import APIRouter, Body, HTTPException
from uuid import UUID, uuid4
from schemas.user import CreateUser, UpdateUser
from core.data import users_db
from crud.user import UserCrud


user_router = APIRouter()


# create a new user
@user_router.post("/users", status_code=201)
def create_user(user: CreateUser = Body(...)):
    new_user = UserCrud.create_user(user)
    return new_user


# update a user
@user_router.patch("/users/{user_id}", status_code=200)
def update_user(user_id: UUID, user: UpdateUser = Body(...)):
    updated_user = UserCrud.update_user(user_id, user)
    return updated_user


# read all users
@user_router.get("/users")
def read_all_users():
    users = UserCrud.read_all_users()
    return users


# read a single user
@user_router.get("/users/{user_id}")
def read_user(user_id: UUID):
    user = UserCrud.read_user(user_id)
    return user


# deactivate a user
@user_router.patch("/users/{user_id}/deactivate")
def deactivate_user(user_id: UUID):
    user = UserCrud.deactivate_user(user_id)
    return user
    # return {"message": "User deactivated successfully"}


# delete a user
@user_router.delete("/users/{user_id}")
def delete_user(user_id: UUID):
    user = UserCrud.delete_user(user_id)
    return user
