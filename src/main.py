from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import Redis

from src.api_routers.auth import auth
from src.api_routers.lists import lists
from src.api_routers.tasks import tasks
from src.config import config
from src.database import Base, engine, session_maker
from src.db_models.user import User


async def insert_admin():
    async with session_maker() as session:
        user = User(username="admin", password="admin")
        session.add(user)
        await session.commit()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await insert_admin()

    redis = Redis(host=config.redis_host, port=config.redis_port)
    FastAPICache.init(RedisBackend(redis), prefix="cache2")
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth)
app.include_router(lists)
app.include_router(tasks)


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
