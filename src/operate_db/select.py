from sqlalchemy import select, text

from src.database import engine, sync_engine
from src.db_models.tables import users


def select_sync() -> list[tuple]:
    query = text("SELECT * FROM users WHERE id > :user_id")
    query = query.bindparams(user_id=20)
    with sync_engine.connect() as conn:
        result = conn.execute(query)
        res = result.all()
    return res


def select_core_sync() -> list[tuple]:
    # SELECT * FROM users
    # query = select(users)

    # SELECT * FROM users WHERE id < 20
    query = select(users).where(users.c.id < 20)
    # filter is same the as where
    # query = select(users).filter(users.columns.id < 20)

    # SELECT * FROM users WHERE id = 17 AND username = 'username_2'
    query = select(users).filter_by(id=17, username="username_2")
    with sync_engine.connect() as conn:
        result = conn.execute(query)
        res = result.all()
    print(res)
    return res


async def select_core() -> list[tuple]:
    # SELECT * FROM users WHERE id = 17 AND username = 'username_2'
    query = select(users).filter_by(id=17, username="username_2")
    async with engine.connect() as conn:
        result = await conn.execute(query)
        res = result.all()
    return res
