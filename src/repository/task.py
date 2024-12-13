from src.db_models.task import Task
from src.repository.base_repo import BaseRepo


class TaskRepo(BaseRepo):
    model = Task
