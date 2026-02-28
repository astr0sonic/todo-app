import uvicorn
from fastapi import FastAPI

from src.config import config

app = FastAPI()


@app.get("/hello")
def say_hello() -> str:
    return "Hello, Woooorld!"


@app.get("/handle")
def handle_data(a: int, b: str) -> str:
    return f"{a=}, {b=}!"


@app.get("/handle/{my_id}")
def handle_my_data(a: int, b: str, my_id: int) -> str:
    return f"{a=}, {b=}, {my_id=}!"


if __name__ == "__main__":
    uvicorn.run("src.main:app", port=config.port, reload=True)
