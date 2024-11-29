from fastapi import APIRouter

from src.models.user import UserRequest, UserResponse

auth = APIRouter(
    prefix="/auth",
    tags=["Registration/authorization"],
)


@auth.post("/sign-up")
async def sign_up(user: UserRequest) -> UserResponse:
    return UserResponse(
        id=1,
        username=user.username,
    )


@auth.post("/sign-in")
async def sign_in(user: UserRequest) -> UserResponse:
    return UserResponse(
        id=1,
        username=user.username,
    )
