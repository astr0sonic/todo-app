import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
async def say_hello() -> str:
    return "Hello, World!!!"


if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True)
