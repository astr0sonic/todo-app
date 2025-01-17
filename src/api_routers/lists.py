import json
from asyncio import sleep
from datetime import datetime, timezone
from typing import List

import jwt
from fastapi import APIRouter, HTTPException, Request, Response, status

# import aioredis
from fastapi_cache.decorator import cache
from redis import Redis

from repository.todo_list import TodoListRepo
from src.config import config
from src.models.task import TaskRequest, TaskResponse
from src.models.todo_list import TodoListRequest, TodoListResponse

lists = APIRouter(
    prefix="/lists",
    tags=["Todo lists processing"],
)


@lists.get("/test_redis")
async def get_my_lists() -> List[str]:
    r = Redis(host=config.redis_host, port=config.redis_port)
    # r = aioredis.from_url(url=f"redis://{config.redis_host}:{config.redis_port}")
    cached_my_data = r.get("cache:mydata")
    if cached_my_data:
        s = json.loads(cached_my_data)
        return s

    await sleep(5)
    my_data = ["my_data_1", "my_data_2", "my_data_3"]
    r.setex("cache:mydata", 10, json.dumps(my_data))
    return my_data


@lists.get("/test_redis2")
@cache(expire=20)
async def get_my_lists2() -> List[str]:
    await sleep(5)
    my_data = ["my_data_1", "my_data_2", "my_data_3"]
    return my_data


@lists.get("")
async def get_lists(request: Request, response: Response) -> List[TodoListResponse]:
    encoded_jwt = request.cookies.get("access_token", "")
    if encoded_jwt == "":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Firstly, you have to log in!",
        )

    try:
        data: dict = jwt.decode(
            jwt=encoded_jwt,
            key=config.secret_key,
            algorithms=[config.signature_algorithm],
        )
    except jwt.InvalidTokenError:
        response.delete_cookie("access_token")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    user_id = int(data.get("sub"))

    if user_id == 1:
        todo_lists = await TodoListRepo.get_all()
        return todo_lists
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access!",
        )


@lists.get("/{list_id}")
async def get_list(list_id: int) -> TodoListResponse | None:
    res = await TodoListRepo.get_by_id(list_id)
    return res


@lists.post("")
async def create_list(todo_list: TodoListRequest) -> TodoListResponse:
    todo_list_id = await TodoListRepo.create(todo_list.model_dump())
    return TodoListResponse(
        id=todo_list_id,
        title=todo_list.title,
        description=todo_list.description,
        user_id=todo_list.user_id,
    )


@lists.put("/{list_id}")
async def update_list(list_id: int, todo_list: TodoListRequest) -> TodoListResponse:
    await TodoListRepo.update(list_id, todo_list)
    return TodoListResponse(
        id=list_id,
        title=todo_list.title,
        description=todo_list.description,
        user_id=todo_list.user_id,
    )


@lists.delete("/{list_id}")
async def delete_list(list_id: int) -> int:
    await TodoListRepo.delete(list_id)
    return list_id


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
