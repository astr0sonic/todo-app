import uvicorn
from fastapi import FastAPI

from src.api_routers.auth import auth_router
from src.api_routers.lists import lists_router
from src.api_routers.other import other_router
from src.api_routers.tasks import tasks_router

app = FastAPI()


@app.get("/hello")
async def say_hello() -> str:
    return "Hello, World!!!"


app.include_router(auth_router)
app.include_router(lists_router)
app.include_router(tasks_router)
app.include_router(other_router)

if __name__ == "__main__":
    uvicorn.run("src.main:app", reload=True, port=8000)
