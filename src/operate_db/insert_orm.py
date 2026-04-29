from time import sleep

from src.database import session_maker, sync_session_maker
from src.db_models.user import User


def insert_sync() -> None:
    with sync_session_maker() as session:
        user = User(username="Eva", password="123")
        session.add(user)
        session.commit()


async def insert() -> None:
    async with session_maker() as session:
        user = User(username="Bob777", password="123")
        session.add(user)
        await session.commit()


async def insert_all() -> None:
    async with session_maker() as session:
        users = [
            User(username="Bob7771", password="123"),
            User(username="Bob7772", password="123"),
        ]
        session.add_all(users)
        await session.commit()


def insert_flush_sync() -> None:
    with sync_session_maker() as session:
        user = User(username="Eva123", password="123")
        session.add(user)
        print(user.id)
        session.flush()
        print(user.id)
        sleep(30)

        session.commit()
