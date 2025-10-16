from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)

from src.config import settings

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("password", String),
)

lists = Table(
    "lists",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("user_id", Integer, ForeignKey("users.id")),
)

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("done", Boolean),
    Column("list_id", Integer, ForeignKey("lists.id")),
)

db_url = settings.sync_db_url()
sync_engine = create_engine(url=db_url)
metadata.drop_all(sync_engine)
metadata.create_all(sync_engine)
