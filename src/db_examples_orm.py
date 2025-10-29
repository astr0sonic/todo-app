import asyncio

from sqlalchemy import create_engine, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.config import settings
from src.database import engine, session_maker, sync_session_maker
from src.db_models.user import User

db_url = settings.sync_db_url
sync_engine = create_engine(url=db_url)


# "INSERT INTO users (username, password) VALUES ('123', '123')
def insert_data_into_users_sync():
    # with Session(sync_engine) as session:
    #     user = User(username="123", password="123")
    #     session.add(user)
    #     session.commit()
    with sync_session_maker() as session:
        user = User(username="123", password="123")
        session.add(user)
        session.commit()


async def insert_data_into_users():
    # async with AsyncSession(engine) as session:
    #     user = User(username="123", password="123")
    #     session.add(user)
    #     await session.commit()
    async with session_maker() as session:
        user = User(username="123", password="123")
        session.add(user)
        await session.commit()


# SELECT * FROM users WHERE id=1
def select_data_from_users_sync():
    with sync_session_maker() as session:
        user_id = 1
        user = session.get(User, user_id)
        if user is not None:
            print(user.id, user.username, user.password)
        else:
            print(f"No user with id={user_id}")


async def select_data_from_users():
    async with session_maker() as session:
        user_id = 10
        user = await session.get(User, user_id)
        if user is not None:
            print(user.id, user.username, user.password)
        else:
            print(f"No user with id={user_id}")


# SELECT * FROM users WHERE id >= 7 AND id <= 9
def complex_select_data_from_users_sync():
    with sync_session_maker() as session:
        query = select(User).where(User.id >= 7).where(User.id <= 9)
        users = session.execute(query)
        for user in users.scalars():
            # print(user[0].id, user[0].username, user[0].password)
            print(user.id, user.username, user.password)
            print()


async def complex_select_data_from_users():
    async with session_maker() as session:
        query = select(User).where(User.id >= 7).where(User.id <= 9)
        users = await session.execute(query)
        for user in users.scalars():
            # print(user[0].id, user[0].username, user[0].password)
            print(user.id, user.username, user.password)
            print()


# UPDATE users SET password = 'qwerty' WHERE id = 3
def update_data_in_users_sync():
    with sync_session_maker() as session:
        user = session.get(User, 3)
        user.password = "qwerty"
        session.commit()


async def update_data_in_users():
    async with session_maker() as session:
        user = await session.get(User, 3)
        user.password = "qwerty123"
        await session.commit()


# update_data_in_users_sync()

asyncio.run(update_data_in_users())
