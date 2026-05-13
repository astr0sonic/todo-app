import json
import logging
import logging.config
import sys
from contextlib import asynccontextmanager

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
from src.operate_db.delete import delete_core, delete_core_sync, delete_sync
from src.operate_db.insert import (
    insert_core,
    insert_sync,
    insert_sync_safe,
    insert_users_sync,
)
from src.operate_db.insert_orm import insert, insert_all, insert_flush_sync, insert_sync
from src.operate_db.select import select_core, select_core_sync, select_sync
from src.operate_db.select_orm import (
    select_complex_orm,
    select_complex_orm_sync,
    select_orm,
    select_orm_sync,
)
from src.operate_db.update import update_core, update_core_sync, update_sync
from src.operate_db.update_orm import (
    update_orm,
    update_orm_refresh_sync,
    update_orm_sync,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await async_create_tables()
    insert_flush_sync()
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


def configure_logging() -> None:
    with open("log.json", "r") as f:
        log_config = json.load(f)
    logging.config.dictConfig(log_config)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.ERROR,
        format="%(asctime)s @-@ %(lineno)s @-@ %(levelname)s --- msg: %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    logger = logging.getLogger("app")
    # logger.propagate = False
    # logger2 = logging.getLogger("app.app1")
    # logger2 -> logger -> root - log propagation
    # logger2.propagate = False
    # logger2.debug("debug")

    logger.setLevel(logging.DEBUG)
    stream_formatter = logging.Formatter(fmt="%(name)s - %(pathname)s - %(message)s")
    file_formatter = logging.Formatter(fmt="%(name)s - %(funcName)s - %(message)s")

    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(stream_formatter)

    file_handler = logging.FileHandler(filename="log.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logger.debug("debug")
    logger.info("info")

    # logging.debug("debug")
    # logging.info("info")
    # logging.warning("warning")
    # logging.error("error")
    # logging.critical("critical")
    # logging.exception("exception")

    # logger handler formatter filter
    # DEBUG INFO WARNING ERROR CRITICAL
    # uvicorn.run("src.main:app", port=config.port, reload=True)

    # custom handler, QueueHandler
