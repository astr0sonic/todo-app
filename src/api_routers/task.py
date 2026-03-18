from fastapi import APIRouter

from models.task import Task

task_router = APIRouter(
    prefix="/tasks",
    tags=["Task"],
)


@task_router.get("{id}")
async def get_task(id: int) -> Task | None: ...


@task_router.put("/{id}")
async def update_task(id: int, task: Task) -> Task | None: ...


@task_router.delete("/{id}")
async def delete_task(id: int) -> int: ...
