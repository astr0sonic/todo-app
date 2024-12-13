from src.db_models.todo_list import TodoList
from src.repository.base_repo import BaseRepo


class TodoListRepo(BaseRepo):
    model = TodoList
