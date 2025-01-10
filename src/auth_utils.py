from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext

from src.config import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(seconds=40)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config.secret_key, algorithm=config.signature_algorithm
    )
    return encoded_jwt
