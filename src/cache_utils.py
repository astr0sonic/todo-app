from src.cache import redis_client

# from typing import Optional


# def get_cache(key: str) -> Optional[str]:
def get_cache(key: str) -> str | None:
    return redis_client.get(key)


def set_cachekey(key: str, value: str, expire: int = 20) -> None:
    redis_client.setex(key, expire, value)
