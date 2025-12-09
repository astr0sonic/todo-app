from src.celery_app import celery_app

# TODO:
# 1. get result
# 2. schedule mode


@celery_app.task
def print_hello():
    return "hello"


@celery_app.task
def add_numbers(a: int, b: int):
    return a + b


result = add_numbers.delay(5, 10)
print(result.get())
