from sqlalchemy import text, update

from src.database import engine, sync_engine
from src.db_models.tables import users


def update_sync() -> None:
    stmt = text(
        "UPDATE users SET username = :username, password = :password WHERE id = :id"
    )
    stmt = stmt.bindparams(**{"username": "bob33", "password": "1234", "id": 43})
    with sync_engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


def update_core_sync() -> None:
    # UPDATE users SET VALUES username = 'bob333' AND password = '12345' WHERE id = 43
    stmt = update(users).values(username="bob333", password="12345").filter_by(id=43)
    with sync_engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


async def update_core() -> None:
    # UPDATE users SET VALUES username = 'bob3333' AND password = '123456' WHERE id = 43
    stmt = update(users).values(username="bob3333", password="123456").filter_by(id=43)
    async with engine.connect() as conn:
        await conn.execute(stmt)
        await conn.commit()
