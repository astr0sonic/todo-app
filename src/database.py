from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import config

engine = create_async_engine(
    url=config.db_url,
)


class Base(DeclarativeBase):
    pass
