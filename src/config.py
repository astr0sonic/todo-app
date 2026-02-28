from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    port: int

    model_config = SettingsConfigDict(env_file=".env")


config = Config()
