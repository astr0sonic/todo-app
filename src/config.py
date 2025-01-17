from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    secret_key: str
    signature_algorithm: str

    redis_host: str
    redis_port: int

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file=".env")


config = Config()
