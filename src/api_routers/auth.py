from fastapi import APIRouter, Request, Response

from src.auth_utils import create_access_token, get_password_hash, verify_password
from src.exceptions import (
    AlreadyRegisteredException,
    InvalidPasswordException,
    UserNotRegisteredException,
)
from src.models.user import UserRequest, UserResponse

auth = APIRouter(
    prefix="/auth",
    tags=["Registration/authorization"],
)

users = [
    {
        "id": 1,
        "username": "admin",
        "hashed_password": "$2b$12$e5n1DjRxYKNuJmjuBj//QOh.XwEej5iteTaAWPFamlXxQULmnxoSO",
    },
]


def get_user(username: str) -> dict | None:
    for user in users:
        if user.get("username") == username:
            return user
    return None


def save_user(username: str, hashed_password: str) -> None:
    user = {
        "id": len(users) + 1,
        "username": username,
        "hashed_password": hashed_password,
    }
    users.append(user)


@auth.post("/sign-up")
async def sign_up(user: UserRequest) -> UserResponse:
    my_user = get_user(username=user.username)
    if my_user is not None:
        raise AlreadyRegisteredException
    hashed_password = get_password_hash(password=user.password)
    save_user(user.username, hashed_password)
    return UserResponse(
        id=len(users),
        username=user.username,
    )


@auth.post("/sign-in")
async def sign_in(request: Request, response: Response, user: UserRequest):
    my_user = get_user(username=user.username)
    if my_user is None:
        raise UserNotRegisteredException
    is_ok = verify_password(
        plain_password=user.password,
        hashed_password=my_user.get("hashed_password"),
    )
    if not is_ok:
        raise InvalidPasswordException

    user_data = {
        "sub": str(my_user.get("id")),
    }
    encoded_jwt = create_access_token(
        data=user_data,
    )
    response.set_cookie(
        key="access_token",
        value=encoded_jwt,
        httponly=True,
    )
    return {
        "access_token": encoded_jwt,
    }


@auth.post("/sign-out")
async def sign_out(response: Response, user: UserRequest):
    # Check if user is logged in
    response.delete_cookie("access_token")
