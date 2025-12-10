from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "celery_tasks",
    broker="redis://localhost:6379",
    backend="redis://localhost:6379",
    # include=["src.celery_tasks"],
)

celery_app.conf.beat_schedule = {
    "sum-every-10-seconds": {
        "task": "src.celery_app.add",
        "schedule": 5.0,
        "args": (1, 10),
        "kwargs": {
            "z": 100,
        },
    },
    "sum-every": {
        "task": "src.celery_app.add",
        "schedule": crontab(minute=30, hour=1),
        "args": (1, 10, 100),
    },
}


@celery_app.task
def add(x: int, y: int, z: int):
    return x + y + z
