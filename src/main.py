from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.api_routers.auth import auth
from src.api_routers.lists import lists
from src.api_routers.tasks import tasks
from src.database import Base, engine
from src.db_models.task import Task
from src.db_models.todo_list import TodoList
from src.db_models.user import User


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth)
app.include_router(lists)
app.include_router(tasks)


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
