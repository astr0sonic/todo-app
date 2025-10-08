from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Registration/Auth"])


@auth_router.post("/sign-up")
async def sign_up():
    return "sign_up"


@auth_router.post("/sign-in")
async def sign_in():
    return "sign_in"
