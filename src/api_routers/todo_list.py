from fastapi import APIRouter

from models.task import Task
from models.todo_list import TodoList

todo_list_router = APIRouter(
    prefix="/lists",
    tags=["Todo List"],
)


@todo_list_router.get("/")
async def get_todo_lists() -> list[TodoList]: ...


@todo_list_router.get("/{id}")
async def get_todo_list(id: int) -> TodoList | None: ...


@todo_list_router.post("/")
async def create_todo_list(todo_list: TodoList) -> TodoList: ...


@todo_list_router.put("/{id}")
async def update_todo_list(id: int, todo_list: TodoList) -> TodoList | None: ...


@todo_list_router.delete("/{id}")
async def delete_todo_list(id: int) -> int: ...


@todo_list_router.get("/lists/{id}/tasks")
async def get_tasks(id: int) -> list[Task]: ...


@todo_list_router.post("/lists/{id}/tasks")
async def create_task(id: int, task: Task) -> Task: ...
