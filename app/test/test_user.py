from unittest.mock import patch
from uuid import UUID, uuid4
import pytest
from fastapi import status
from fastapi.testclient import TestClient


from main import app


client = TestClient(app)


@pytest.fixture
def mock_users_db():
    return {
        "860d7a5b-70e2-449a-a012-06df989659e7": {
            "username": "oliver",
            "full_name": "oliver queen",
            "email": "oliverqueen@gmail.com",
            "is_active": True,
        },
        "7e76cleed": {
            "username": "Berry",
            "full_name": "Berry Allen",
            "email": "berryallen@gmail.com",
            "is_active": True,
        },
        "7e76cnddd": {
            "username": "felicity",
            "full_name": "felicity smoak",
            "email": "felicitysmoak@gmail.com",
            "is_active": False,
        },
    }


# Test create user
@patch("crud.user.UserCrud.create_user")
def test_create_user(mock_create_user):
    # input data from the user
    mock_user = {
        "username": "testuser",
        "full_name": "Test User",
        "email": "testuser@gmail.com",
    }
    mock_create_user.return_value = {
        "user_id": str(uuid4()),
        "full_name": "Test User",
        "email": "testuser@gmail.com",
        "is_active": True,
    }

    # Simulating a POST request to create a user
    response = client.post(
        "/v1/users",
        json=mock_user,
    )

    # Assertions
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == mock_create_user.return_value
    assert mock_create_user.called  # Ensure `create_user` was called


# Test read all users
@patch("crud.user.UserCrud.read_all_users")
def test_read_all_users(mock_read_all_users):
    # input data from the user
    mock_read_all_users.return_value = [
        {
            "user_id": str(uuid4()),
            "full_name": "berry allen",
            "email": "someemail@gmail.com",
            "is_active": True,
        },
        {
            "user_id": str(uuid4()),
            "full_name": "felicity smoak",
            "email": "felicitysmoak@gmail.com",
            "is_active": False,
        },
        {
            "user_id": str(uuid4()),
            "full_name": "oliver queen",
            "email": "oliverqueen@gmail.com",
            "is_active": True,
        },
    ]

    # Simulating a GET request to read all users
    response = client.get("/v1/users")

    # Assertions
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mock_read_all_users.return_value


# Test read a single user
@patch("crud.user.UserCrud.read_user")
def test_read_user(mock_read_user):
    # input data from the user
    mock_uuid = str(uuid4())

    mock_read_user.return_value = {
        "user_id": str(UUID),
        "full_name": "berry allen",
        "email": "berryallen@gmail.com",
        "is_active": True,
    }
    # Simulating a GET request to read a single user
    response = client.get(f"/v1/users/{mock_uuid}")

    # Assertions
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mock_read_user.return_value


# Test Update user
@patch("crud.user.UserCrud.update_user")
def test_update_user(mocked_update_user):
    user_id = "860d7a5b-70e2-449a-a012-06df989659e7"

    mock_user = {
        "username": "testuser",
        "full_name": "Test User",
        "email": "updateuseremail@gmail.com",
    }

    mocked_update_user.return_value = {
        user_id: {
            "username": "testuser",
            "full_name": "Test User",
            "email": "updateemail",
            "is_active": True,
        },
    }

    # Simulating a PATCH request to update a user
    response = client.patch(f"/v1/users/{user_id}", json=mock_user)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mocked_update_user.return_value


# Test deactivate user v2
@patch("crud.user.UserCrud.deactivate_user")
def test_deactivate_user(mocked_deactivate_user, mock_users_db):

    user_id = "860d7a5b-70e2-449a-a012-06df989659e7"

    mock_users_db["860d7a5b-70e2-449a-a012-06df989659e7"]["is_active"] = False

    mocked_deactivate_user.return_value = {
        "username": mock_users_db["860d7a5b-70e2-449a-a012-06df989659e7"]["username"],
        "email": mock_users_db["860d7a5b-70e2-449a-a012-06df989659e7"]["email"],
        "is_active": False,
        "message": "User deactivated successfully",
    }

    # Simulating a PATCH request to update a user
    response = client.patch(f"/v1/users/{user_id}/deactivate")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == mocked_deactivate_user.return_value
    assert mock_users_db["860d7a5b-70e2-449a-a012-06df989659e7"]["is_active"] is False


# deactivate user
# @patch("crud.user.UserCrud.deactivate_user")
# def test_deactivate_user(mocked_deactivate_user):

#     user_id = "860d7a5b-70e2-449a-a012-06df989659e7"

#     mocked_deactivate_user.return_value = {
#         "username": "testuser",
#         "email": "updateuseremail@gmail.com",
#         "is_active": False,
#         "message": "User deactivated successfully",
#     }

#     # Simulating a PATCH request to update a user
#     response = client.put(f"/v1/users/{user_id}/deactivate")
#     response_data = response.json()

#     assert response.status_code == status.HTTP_200_OK
#     assert "error" not in response_data
#     assert response.json() == mocked_deactivate_user.return_value
#     assert
#     # assert response_data.get("message") == "User deactivated successfully"


@patch("crud.user.UserCrud.delete_user")
def test_delete_user(mocked_delete_user, mock_users_db):

    user_id = "860d7a5b-70e2-449a-a012-06df989659e7"

    del mock_users_db[user_id]

    mocked_delete_user.return_value = {
        "message": "User deleted successfully",
    }

    # Simulating a PATCH request to update a user
    response = client.delete(f"/v1/users/{user_id}")
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert "error" not in response_data
    assert response.json() == mocked_delete_user.return_value
    assert user_id not in mock_users_db
