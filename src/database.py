import asyncio

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import settings


async def connect_db():
    # db+driver://db_user:db_password@db_host:db_port/db_name
    db_url = settings.sync_db_url
    sync_engine = create_engine(url=db_url)

    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT VERSION()"))
        print(res.one()[0])
        if not res.closed:
            print(res.one()[0])

    db_url = settings.db_url
    engine = create_async_engine(url=db_url)

    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(res.one()[0])


asyncio.run(connect_db())


class Base(DeclarativeBase):
    pass


db_url = settings.db_url
engine = create_async_engine(url=db_url)
session_maker = async_sessionmaker(engine)

sync_db_url = settings.sync_db_url
sync_engine = create_engine(url=sync_db_url)
sync_session_maker = sessionmaker(sync_engine)
