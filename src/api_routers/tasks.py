from fastapi import APIRouter

tasks_router = APIRouter(prefix="/tasks", tags=["Processing tasks"])


@tasks_router.get("/{task_id}")
async def get_task(task_id: int):
    return "get_task"


@tasks_router.put("/{task_id}")
async def update_task(task_id: int):
    return "update_task"


@tasks_router.delete("/{task_id}")
async def delete_task(task_id: int):
    return "delete_task"
