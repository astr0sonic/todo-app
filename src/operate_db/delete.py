from sqlalchemy import delete, text

from src.database import engine, sync_engine
from src.db_models.tables import users


def delete_sync() -> None:
    stmt = text("DELETE FROM users WHERE id = :id")
    stmt = stmt.bindparams(**{"id": 37})
    with sync_engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


def delete_core_sync() -> None:
    # DELETE FROM users WHERE id = 38
    stmt = delete(users).filter_by(id=38)
    with sync_engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()


async def delete_core() -> None:
    # DELETE FROM users WHERE id = 39
    stmt = delete(users).filter_by(id=39)
    async with engine.connect() as conn:
        await conn.execute(stmt)
        await conn.commit()
