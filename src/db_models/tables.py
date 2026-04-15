from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
)

from src.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(255), unique=True),
    Column("password", String(255)),
)

lists = Table(
    "lists",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("description", String),
    Column("user_id", Integer, ForeignKey("users.id")),
)

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(255)),
    Column("description", String),
    Column("done", Boolean),
    Column("list_id", Integer, ForeignKey("lists.id")),
)
