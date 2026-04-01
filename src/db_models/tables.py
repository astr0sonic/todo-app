from enum import unique

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

from src.config import config

metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(255), unique=True),
    Column("password", String(255)),
)

lists = Table(
    "lists",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("description", String),
    Column("user_id", Integer, ForeignKey("users.id")),
)

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("description", String),
    Column("done", Boolean),
    Column("list_id", Integer, ForeignKey("lists.id")),
)


def create_tables() -> None:
    engine = create_engine(config.sync_db_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)


async def async_create_tables() -> None:
    engine = create_async_engine(config.db_url)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
