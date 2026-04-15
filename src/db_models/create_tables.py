from sqlalchemy.ext.asyncio import create_async_engine

from src.config import config
from src.database import Base, create_engine, metadata
from src.db_models.tables import lists, tasks, users
from src.db_models.task import Task
from src.db_models.todo_list import TodoList
from src.db_models.user import User


def create_tables_core() -> None:
    engine = create_engine(config.sync_db_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)


async def async_create_tables_core() -> None:
    engine = create_async_engine(config.db_url)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


def create_tables() -> None:
    engine = create_engine(config.sync_db_url, echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


async def async_create_tables() -> None:
    engine = create_async_engine(config.db_url, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
