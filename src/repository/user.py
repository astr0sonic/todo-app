from src.db_models.user import User
from src.repository.base_repo import BaseRepo


class UserRepo(BaseRepo):
    model = User
