import asyncio

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import settings
from src.database import Base
from src.db_models.task import Task
from src.db_models.todo_list import TodoList
from src.db_models.user import User


def sync_create_tables() -> None:
    db_url = settings.sync_db_url
    sync_engine = create_engine(url=db_url)
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


async def create_tables() -> None:
    db_url = settings.db_url
    engine = create_async_engine(url=db_url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(create_tables())
