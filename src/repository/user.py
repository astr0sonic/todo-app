from src.db_models.user import User
from src.repository.base import BaseRepository


class Repository(BaseRepository):
    db_model = User
