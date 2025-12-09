from celery import Celery

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379",
    backend="redis://localhost:6379",
    # include=["src.tasks"],
)

# celery -A src.celery_app:celery_app worker --loglevel=info
# celery -A src.tasks:celery beat --loglevel=info

# celery_app.conf.beat_schedule = {
#     'print-every-5-seconds': {
#         'task': 'tasks.add',
#         'schedule': 5.0,
#         'args': ()
#     },
# }
# celery_app.conf.timezone = 'UTC'


@celery_app.task
def print_hello():
    return "hello"


print_hello.delay()
