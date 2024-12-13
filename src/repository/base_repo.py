from sqlalchemy import select

from src.database import session_maker


class BaseRepo:
    model = None

    @classmethod
    async def get_by_id(cls, id):
        async with session_maker() as session:
            # query = select(TodoList).where(TodoList.id == list_id)
            # query = select(TodoList).filter(TodoList.id == list_id)
            # query = select(TodoList).filter_by(id=list_id)
            # result = await session.execute(query)
            # res = result.scalars().one_or_none()
            res = await session.get(cls.model, id)
        return res

    @classmethod
    async def get_all(cls):
        async with session_maker() as session:
            query = select(cls.model)  # SELECT * FROM lists
            result = await session.execute(query)
            res = result.scalars().all()
        return res

    @classmethod
    async def create(cls, data: dict):
        async with session_maker() as session:
            my_model = cls.model(**data)
            session.add(my_model)
            await session.flush()  # expire и refresh
            # session.add_all([my_todo_list, my_todo_list])
            my_model_id = my_model.id
            await session.commit()
        return my_model_id

    @classmethod
    async def update(cls, list_id: int, data: dict):
        async with session_maker() as session:
            my_model = await session.get(cls.model, list_id)
            # TODO: implement...
            await session.commit()

    @classmethod
    async def delete(cls, list_id: int):
        async with session_maker() as session:
            my_model = await session.get(cls.model, list_id)
            await session.delete(my_model)
            await session.commit()
