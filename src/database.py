from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import config

engine = create_async_engine(
    url=config.db_url,
)

session_maker = async_sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
