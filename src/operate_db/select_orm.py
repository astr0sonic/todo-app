from typing import Optional

from sqlalchemy import select

from src.database import session_maker, sync_session_maker
from src.db_models.user import User


# def select_sync() -> Optinal[User]:
def select_orm_sync() -> User | None:
    with sync_session_maker() as session:
        user = session.get(User, 100)
    return user


async def select_orm() -> User | None:
    async with session_maker() as session:
        user = await session.get(User, 48)
    return user


def select_complex_orm_sync() -> list[User]:
    with sync_session_maker() as session:
        # SELECT * FROM users WHERE id > 22
        # query = select(User).filter(User.id > 22)
        query = select(User).where(User.id > 22)
        result = session.execute(query)
        users = result.scalars().all()
    return users


async def select_complex_orm() -> list[User]:
    async with session_maker() as session:
        # SELECT * FROM users WHERE username = 'admin'
        query = select(User).filter_by(username="admin")
        result = await session.execute(query)
        users = result.scalars().all()
    return users
