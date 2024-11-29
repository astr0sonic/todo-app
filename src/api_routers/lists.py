from typing import List

from fastapi import APIRouter
from sqlalchemy import select

from src.database import session_maker
from src.db_models.todo_list import TodoList
from src.models.task import TaskRequest, TaskResponse
from src.models.todo_list import TodoListRequest, TodoListResponse

lists = APIRouter(
    prefix="/lists",
    tags=["Todo lists processing"],
)


@lists.get("")
async def get_lists() -> List[TodoListResponse]:
    async with session_maker() as session:
        query = select(TodoList)  # SELECT * FROM lists
        result = await session.execute(query)
        res = result.scalars().all()
    return res


@lists.get("/{list_id}")
async def get_list(list_id: int) -> TodoListResponse | None:
    async with session_maker() as session:
        # query = select(TodoList).where(TodoList.id == list_id)
        # query = select(TodoList).filter(TodoList.id == list_id)
        # query = select(TodoList).filter_by(id=list_id)
        # result = await session.execute(query)
        # res = result.scalars().one_or_none()

        res = await session.get(TodoList, list_id)
    return res


@lists.post("")
async def create_list(todo_list: TodoListRequest) -> TodoListResponse:
    async with session_maker() as session:
        my_todo_list = TodoList(
            title=todo_list.title,
            description=todo_list.description,
            user_id=todo_list.user_id,
        )
        session.add(my_todo_list)
        # session.add_all([my_todo_list, my_todo_list])
        await session.commit()

    return TodoListResponse(
        id=1,
        title=todo_list.title,
        description=todo_list.description,
        user_id=todo_list.user_id,
    )


@lists.put("/{list_id}")
async def update_list(list_id: int, todo_list: TodoListRequest) -> str:
    return TodoListResponse(
        id=list_id,
        title=todo_list.title,
        description=todo_list.description,
        user_id=todo_list.user_id,
    )


@lists.delete("/{list_id}")
async def delete_list(list_id: int) -> TodoListResponse:
    return TodoListResponse(
        id=list_id,
        title=f"My list {list_id}",
        description="My description",
        user_id=1,
    )


@lists.post("/{list_id}/tasks")
async def create_task(list_id: int, task: TaskRequest) -> TaskResponse:
    return TaskResponse(
        id=1,
        title=task.title,
        description=task.title,
        done=task.done,
        list_id=list_id,
    )


@lists.get("/{list_id}/tasks")
async def get_tasks(list_id: int) -> List[TaskResponse]:
    return [
        TaskResponse(
            id=1,
            title="Task 1",
            description="My task",
            done=False,
            list_id=list_id,
        ),
        TaskResponse(
            id=2,
            title="Task 2",
            description="My task",
            done=False,
            list_id=list_id,
        ),
    ]
