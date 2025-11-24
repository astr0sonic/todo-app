import datetime
from datetime import timedelta

from authx import AuthX, AuthXConfig
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from jose import jwt

from src.models.user import UserRequest, UserResponse

auth_router = APIRouter(prefix="/auth", tags=["Registration/Auth"])

# идентификация
# аутентификация
# авторизация

SECRET_KEY = "123456"

### authx

config = AuthXConfig(
    JWT_ALGORITHM="HS256",
    JWT_SECRET_KEY=SECRET_KEY,
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_TOKEN_LOCATION=["cookies"],
)

authx = AuthX(config=config)


users = []


@auth_router.post("/sign-up")
async def sign_up(user: UserRequest) -> UserResponse:
    user_obj = {
        "id": len(users) + 1,
        "username": user.username,
        "password": user.password,
    }
    users.append(user_obj)
    return UserResponse(
        user_id=user_obj.get("id"),
        username=user.username,
    )


@auth_router.post("/sign-in")
async def sign_in(user: UserRequest, response: Response) -> str:
    for user_obj in users:
        if user_obj.get("username") == user.username:
            # access_token = create_access_token(user_obj)
            access_token = authx.create_access_token(uid=str(user_obj.get("id")))
            response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, access_token)
            return access_token
    raise HTTPException(status_code=401, detail="Incorrect username/password")


@auth_router.get("/protected", dependencies=[Depends(authx.access_token_required)])
# async def protected(user: UserRequest, request: Request) -> str:
async def protected() -> dict:
    # access_token = request.cookies.get("access_token", "NOT_FOUND")
    # if access_token == "NOT_FOUND":
    #     raise HTTPException(status_code=403, detail="You are not alloweed")
    # res = jwt.decode(access_token, SECRET_KEY, "HS256")
    # return str(res)
    return {"result": "secret data"}


def create_access_token(payload: dict) -> str:
    expire = datetime.datetime.now() + timedelta(minutes=30)
    expire = expire.timestamp()
    encoded_jwt = jwt.encode(
        {
            "user_id": payload.get("id"),
            "username": payload.get("username"),
            "expire": int(expire),
        },
        SECRET_KEY,
        "HS256",
    )
    return encoded_jwt
