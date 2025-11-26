import json
from asyncio import sleep as async_sleep
from time import sleep
from typing import Optional

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from src.cache_utils import get_cache, set_cachekey
from src.models.task import TaskRequest, TaskResponse
from src.models.todo_list import TodoListRequest, TodoListResponse
from src.repository.todo_list import Repository

lists_router = APIRouter(prefix="/lists", tags=["Processing todo lists"])


@lists_router.get("/test_redis")
def test_redis() -> list[str]:
    if get_cache("mydata"):
        res = get_cache("mydata")
        res = json.loads(res)
        return res
    mydata = ["one", "two", "three"]
    set_cachekey("mydata", json.dumps(mydata))
    sleep(3)
    return mydata


@lists_router.get("/test_redis2")
@cache(expire=20)
async def test_redis2() -> list[str]:
    mydata = ["one", "two", "three"]
    await async_sleep(3)
    return mydata


@lists_router.post("")
async def create_list(todo_list: TodoListRequest) -> TodoListResponse:
    return TodoListResponse(
        list_id=1,
        title=todo_list.title,
    )


@lists_router.get("")
async def get_lists() -> list[TodoListResponse]:
    return [
        TodoListResponse(list_id=1, title="My title 1"),
        TodoListResponse(list_id=2, title="My title 2"),
    ]


@lists_router.get("/{list_id}")
async def get_list(list_id: int) -> Optional[TodoListResponse]:
    # async with session_maker() as session:
    #     todo_list = await session.get(TodoList, list_id)
    # TODO: model_validate - different attribute names
    # todo_list_response = TodoListResponse.model_validate(todo_list, from_attributes=True)

    todo_list_repo = Repository()
    todo_list = await todo_list_repo.get_by_id(list_id)
    if todo_list is not None:
        return TodoListResponse(
            list_id=todo_list.id,
            title=todo_list.description,
        )
    return None


@lists_router.put("/{list_id}")
async def update_list(list_id: int, todo_list: TodoListRequest) -> TodoListResponse:
    return TodoListResponse(
        list_id=list_id,
        title=todo_list.title,
    )


@lists_router.delete("/{list_id}")
async def delete_list(list_id: int) -> int:
    repo = Repository()
    await repo.delete(list_id)
    return list_id


@lists_router.post("/{list_id}/tasks")
async def create_task(list_id: int, task: TaskRequest) -> TaskResponse:
    return TaskResponse(
        task_id=1,
        title=task.title,
    )


@lists_router.get("/{list_id}/tasks")
async def get_tasks(list_id: int) -> list[TaskResponse]:
    return [
        TaskResponse(task_id=1, title="My title"),
    ]
