import asyncio

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import settings

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(255)),
    Column("password", String(255)),
)

lists = Table(
    "lists",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("user_id", Integer, ForeignKey("users.id")),
)

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("done", Boolean),
    Column("list_id", Integer, ForeignKey("lists.id")),
)


def sync_create_tables() -> None:
    db_url = settings.sync_db_url
    sync_engine = create_engine(url=db_url)
    metadata.drop_all(sync_engine)
    metadata.create_all(sync_engine)


async def create_tables() -> None:
    db_url = settings.db_url
    engine = create_async_engine(url=db_url)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


# asyncio.run(create_tables())
