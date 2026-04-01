from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.database import Base


class User(Base):
    __tablename__ = "users"

    # id: Mapped[int] = Column("id", Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))
