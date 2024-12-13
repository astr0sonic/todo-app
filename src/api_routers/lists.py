from typing import List

from fastapi import APIRouter

from repository.todo_list import TodoListRepo
from src.models.task import TaskRequest, TaskResponse
from src.models.todo_list import TodoListRequest, TodoListResponse

lists = APIRouter(
    prefix="/lists",
    tags=["Todo lists processing"],
)


@lists.get("")
async def get_lists() -> List[TodoListResponse]:
    todo_lists = await TodoListRepo.get_all()
    return todo_lists


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
