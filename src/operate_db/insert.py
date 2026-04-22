from sqlalchemy import insert, text

from src.database import engine, sync_engine
from src.db_models.tables import users


def insert_sync() -> None:
    username = "admin"
    password = "admin"
    with sync_engine.connect() as conn:
        conn.execute(
            text(
                f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
            )
        )
        conn.commit()


def insert_sync_safe() -> None:
    username = "admin1"
    password = "admin1"
    stmt = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    stmt = stmt.bindparams(**{"username": username, "password": password})
    with sync_engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


def insert_users_sync() -> None:
    stmt = text("INSERT INTO users (username, password) VALUES (:u1, :p1), (:u2, :p2)")
    vals = {
        "u1": "username_1",
        "u2": "username_2",
        "p1": "p1",
        "p2": "p2",
    }
    stmt = stmt.bindparams(**vals)
    print(stmt.compile(compile_kwargs={"literal_binds": True}))
    with sync_engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


async def insert_core() -> None:
    stmt = insert(users).values(username="bob3", password="123")
    async with engine.connect() as conn:
        await conn.execute(stmt)
        await conn.commit()
