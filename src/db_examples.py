import asyncio

from sqlalchemy import delete, insert, select, text, update

from src.database import engine
from src.db_models.tables import users


async def insert_data_into_users() -> None:
    username = "qwe1"
    password = "rty1"
    stmt = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    stmt = stmt.bindparams(username=username, password=password)
    # stmt = stmt.bindparams(**{
    #     "username": username,
    #     "password": password,
    # })
    print(stmt.compile(compile_kwargs={"literal_binds": True}))

    # async with engine.begin() as conn:
    async with engine.connect() as conn:
        await conn.execute(stmt)
        await conn.commit()


async def insert_data_into_users_core() -> None:
    username = "qwe55"
    password = "rty66"
    # stmt = insert(users).values(username=username, password=password)
    stmt = insert(users).values({"username": username, "password": password})

    async with engine.connect() as conn:
        await conn.execute(stmt)
        await conn.commit()


async def select_data_from_users() -> None:
    query = text("SELECT * FROM users")

    async with engine.connect() as conn:
        res = await conn.execute(query)
        # for obj in res:
        #     print(obj)

        # one, one_or_none, all
        print(res.all())


async def select_data_from_users_core() -> None:
    query = select(users).where(users.c.username == "qwe222")
    # query = select(users).filter(
    #     users.c.username == "qwe222"
    # )

    # query = select(users).filter_by(username="qwe222")

    async with engine.connect() as conn:
        res = await conn.execute(query)
        print(res.all())


async def update_data_in_users() -> None:
    query = text("UPDATE users SET password = :password WHERE id = :id")
    query = query.bindparams(password="123456", id=1)

    async with engine.connect() as conn:
        await conn.execute(query)
        await conn.commit()


async def update_data_in_users_core() -> None:
    query = update(users).values(password="zxcvb1").filter_by(id=1)

    async with engine.connect() as conn:
        await conn.execute(query)
        await conn.commit()


async def delete_data_in_users() -> None:
    query = text("DELETE FROM users WHERE id = :id")
    query = query.bindparams(id=1)

    async with engine.connect() as conn:
        await conn.execute(query)
        await conn.commit()


async def delete_data_in_users_core() -> None:
    query = delete(users).filter_by(id=2)

    async with engine.connect() as conn:
        await conn.execute(query)
        await conn.commit()


asyncio.run(delete_data_in_users_core())
