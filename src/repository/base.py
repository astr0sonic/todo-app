from sqlalchemy import select

from src.database import session_maker


class BaseRepository:
    db_model = None

    @classmethod
    async def get_by_id(cls, list_id: int):
        async with session_maker() as session:
            todo_list = await session.get(cls.db_model, list_id)
        return todo_list

    async def get(cls, **criteria):
        async with session_maker() as session:
            query = select(cls.db_model).filter_by(**criteria)
            lists = await session.execute(query)
        lists = lists.scalars()
        return lists

    async def create(cls, data: dict):
        async with session_maker() as session:
            todo_list = cls.db_model(**data)
            session.add(todo_list)
            await session.commit()

    async def delete(cls, list_id: int):
        async with session_maker() as session:
            todo_list = await session.get(cls.db_model, list_id)
            await session.delete(todo_list)
            await session.commit()

    async def update(cls, list_id: int, data: dict):
        async with session_maker() as session:
            todo_list = await session.get(cls.db_model, list_id)
            for key in data.keys():
                setattr(todo_list, key, data[key])
            await session.commit()
