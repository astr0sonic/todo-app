from pydantic import BaseModel


class TodoListRequest(BaseModel):
    title: str
    description: str


class TodoListResponse(BaseModel):
    list_id: int
    title: str
