from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str = "FleetVision AI"

    VERSION: str = "1.0.0"

    API_V1_STR: str = "/api/v1"

    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    POSTGRES_DB: str

    POSTGRES_HOST: str

    POSTGRES_PORT: int

    REDIS_HOST: str

    REDIS_PORT: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings():

    return Settings()


settings = get_settings()