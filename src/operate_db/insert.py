from sqlalchemy import text

from src.database import sync_engine


def insert_sync() -> None:
    username = "admin"
    password = "admin"
    with sync_engine.connect() as conn:
        conn.execute(
            text(
                f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
            )
        )
        conn.commit()
