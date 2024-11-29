from fastapi import APIRouter
from sqlalchemy import text

from src.database import Base, engine
from src.db_models.task import Task
from src.db_models.todo_list import TodoList
from src.db_models.user import User
from src.models.user import UserRequest, UserResponse

auth = APIRouter(
    prefix="/auth",
    tags=["Registration/authorization"],
)


@auth.post("/sign-up")
async def sign_up(user: UserRequest) -> UserResponse:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

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
