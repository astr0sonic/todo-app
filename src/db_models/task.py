from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    done: Mapped[bool]
    list_id: Mapped[int] = mapped_column(ForeignKey("lists.id"))

    # todo_list: Mapped["TodoList"] = relationship(back_populates="tasks")
