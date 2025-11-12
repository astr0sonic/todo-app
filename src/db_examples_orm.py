import asyncio

from sqlalchemy import create_engine, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.config import settings
from src.database import engine, session_maker, sync_session_maker
from src.db_models.task import Task
from src.db_models.todo_list import TodoList
from src.db_models.user import User
from src.models import todo_list

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
        # user = User(username="asd", password="asd")
        # session.add(user)
        # print(user.id)
        # await session.flush()
        # print(user.id)
        # await asyncio.sleep(30)
        # await session.commit()

        # user = User(username="5556", password="6666")
        # session.add(user)
        # # TODO: expire_all
        # session.expire_all()
        # await session.commit()

        user = await session.get(User, 12)
        print(user)
        await asyncio.sleep(30)
        await session.refresh(user)
        print(user.username)


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


# DELETE FROM users WHERE id = 4
def delete_data_in_users_sync():
    with sync_session_maker() as session:
        user = session.get(User, 5)
        session.delete(user)
        session.commit()


async def delete_data_in_users():
    async with session_maker() as session:
        user = await session.get(User, 6)
        await session.delete(user)
        await session.commit()


async def insert_data():
    async with session_maker() as session:
        todo_list = await session.get(TodoList, 1)
        task1 = Task(title="Task1", description="d1", done=False, list_id=todo_list.id)
        task2 = Task(title="Task2", description="d2", done=False, list_id=todo_list.id)
        task3 = Task(title="Task3", description="d3", done=False, list_id=todo_list.id)
        session.add_all([task1, task2, task3])
        await session.commit()


def get_todo_list_sync():
    with sync_session_maker() as session:
        todo_list = session.get(TodoList, 1)
        print(todo_list.tasks)


async def get_todo_list():
    async with session_maker() as session:
        todo_list = await session.get(TodoList, 1)
        print(todo_list.tasks)


# delete_data_in_users_sync()

asyncio.run(delete_data_in_users())
