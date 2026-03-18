from pydantic import BaseModel


class TodoList(BaseModel):
    id: int | None = None
    title: str
    description: str
