from src.db_models.task import Task
from src.repository.base import BaseRepository


class Repository(BaseRepository):
    db_model = Task
