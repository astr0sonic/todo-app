from fastapi import APIRouter

from src.models.user import UserRequest, UserResponse

auth_router = APIRouter(prefix="/auth", tags=["Registration/Auth"])

# идентификация
# аутентификация
# авторизация


@auth_router.post("/sign-up")
async def sign_up(user: UserRequest) -> UserResponse:
    return UserResponse(
        user_id=1,
        username=user.username,
    )


@auth_router.post("/sign-in")
async def sign_in(user: UserRequest) -> UserResponse:
    return UserResponse(
        user_id=1,
        username=user.username,
    )
