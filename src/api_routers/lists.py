from fastapi import APIRouter

from src.database import session_maker
from src.db_models.todo_list import TodoList
from src.models.task import TaskRequest, TaskResponse
from src.models.todo_list import TodoListRequest, TodoListResponse

lists_router = APIRouter(prefix="/lists", tags=["Processing todo lists"])


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
async def get_list(list_id: int) -> TodoListResponse:
    # repo = Repository()
    # todo_list = await repo.get_todo_list(list_id=1)
    async with session_maker() as session:
        todo_list = await session.get(TodoList, list_id)
    # TODO: model_validate - different attribute names
    # todo_list_response = TodoListResponse.model_validate(todo_list, from_attributes=True)
    return TodoListResponse(
        list_id=todo_list.id,
        title=todo_list.description,
    )


@lists_router.put("/{list_id}")
async def update_list(list_id: int, todo_list: TodoListRequest) -> TodoListResponse:
    return TodoListResponse(
        list_id=list_id,
        title=todo_list.title,
    )


@lists_router.delete("/{list_id}")
async def delete_list(list_id: int) -> TodoListResponse:
    return TodoListResponse(
        list_id=list_id,
        title="My title",
    )


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
