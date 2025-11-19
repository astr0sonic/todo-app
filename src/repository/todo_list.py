from src.db_models.todo_list import TodoList
from src.repository.base import BaseRepository


class Repository(BaseRepository):
    db_model = TodoList
