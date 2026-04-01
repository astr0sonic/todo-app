from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import config


class Base(DeclarativeBase):
    pass


def connect_db() -> None:
    engine = create_engine(config.sync_db_url)

    with engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION()"))
        print(res.one()[0])


async def async_connect_db() -> None:
    engine = create_async_engine(config.db_url)

    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(res.one()[0])
