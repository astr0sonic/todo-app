from fastapi import APIRouter

from src.models.task import TaskRequest, TaskResponse

tasks_router = APIRouter(prefix="/tasks", tags=["Processing tasks"])


@tasks_router.get("/{task_id}")
async def get_task(task_id: int) -> TaskResponse:
    return TaskResponse(
        task_id=1,
        title="My title",
    )


@tasks_router.put("/{task_id}")
async def update_task(task_id: int, task: TaskRequest) -> TaskResponse:
    return TaskResponse(
        task_id=task_id,
        title=task.title,
    )


@tasks_router.delete("/{task_id}")
async def delete_task(task_id: int) -> TaskResponse:
    return TaskResponse(
        task_id=task_id,
        title="My title",
    )
