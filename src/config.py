from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    @property
    def sync_db_url(self) -> str:
        return f"postgresql+psycopg2://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
