from time import sleep

from src.database import session_maker, sync_session_maker
from src.db_models.user import User


def update_orm_sync() -> None:
    with sync_session_maker() as session:
        user = session.get(User, 26)
        user.password = "123456"
        session.commit()
    return user


async def update_orm() -> None:
    async with session_maker() as session:
        user = await session.get(User, 3)
        user.password = "123"
        await session.commit()
    return user


def update_orm_refresh_sync() -> None:
    with sync_session_maker() as session:
        user = session.get(User, 26)
        print(user.username)
        sleep(30)
        session.refresh(user)
        print(user.username)
        user.password = "123456"
        session.commit()
    return user
