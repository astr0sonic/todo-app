from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)  # username VARCHAR NOT NULL
    password: Mapped[str] = mapped_column(nullable=False)

    lists: Mapped[List["TodoList"]] = relationship(back_populates="user")
