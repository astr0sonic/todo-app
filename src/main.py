from contextlib import asynccontextmanager
from venv import create

import uvicorn
from fastapi import APIRouter, FastAPI

from src.api_routers.auth import auth_router
from src.api_routers.task import task_router
from src.api_routers.todo_list import todo_list_router
from src.config import config
from src.db_models.create_tables import (
    async_create_tables,
    create_tables,
    create_tables_core,
)
from src.operate_db.insert import insert_sync


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await async_create_tables()
    insert_sync()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(todo_list_router)
app.include_router(task_router)


@app.get("/hello")
def say_hello() -> str:
    return "Hello, Woooorld!"


@app.get("/handle")
def handle_data(a: int, b: str) -> str:
    return f"{a=}, {b=}!"


@app.get("/handle/{my_id}")
def handle_my_data(a: int, b: str, my_id: int) -> str:
    return f"{a=}, {b=}, {my_id=}!"


if __name__ == "__main__":
    uvicorn.run("src.main:app", port=config.port, reload=True)
