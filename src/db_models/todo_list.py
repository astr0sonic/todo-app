from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class TodoList(Base):
    __tablename__ = "lists"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # tasks: Mapped[List["Task"]] = relationship(primaryjoin="TodoList.id == Task.list_id", lazy="selectin")
    # tasks: Mapped[List["Task"]] = relationship(primaryjoin="and_(TodoList.id == Task.list_id, TodoList.id == Task.list_id)", lazy="selectin")

    # joined - M:1, 1:1
    # selectin - M:M, 1:M
