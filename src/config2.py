import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Settings:
    db_username: str
    db_password: str
    db_port: int


load_dotenv()

db_username = os.getenv("DB_USERNAME")
if db_username is None:
    print("DB_USERNAME is not set")
    exit(1)

db_password = os.getenv("DB_PASSWORD")
if db_password is None:
    print("DB_PASSWORD is not set")
    exit(1)

db_port = os.getenv("DB_PORT")
if db_port is None:
    print("DB_PORT is not set")
    exit(1)

settings = Settings(
    db_username=db_username,
    db_password=db_password,
    db_port=int(db_port),
)
