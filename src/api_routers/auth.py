from fastapi import APIRouter

from models.user import User

auth_router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@auth_router.post("/sign-up")
async def sign_up(user: User) -> User | None: ...


@auth_router.post("/sign-in")
async def sign_in(user: User) -> User | None: ...
