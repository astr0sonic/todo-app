from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import config

metadata = MetaData()


class Base(DeclarativeBase):
    pass


sync_engine = create_engine(config.sync_db_url)
sync_session_maker = sessionmaker(bind=sync_engine)

engine = create_async_engine(config.db_url)
session_maker = async_sessionmaker(bind=engine)


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
