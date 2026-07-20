from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    """
    FleetVision AI application settings.

    Values are loaded from environment variables
    or a .env file.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # =====================================================
    # Application
    # =====================================================

    APP_NAME: str = "FleetVision AI"

    APP_VERSION: str = "1.0.0"

    DEBUG: bool = True

    ENVIRONMENT: str = "development"

    # =====================================================
    # Security
    # =====================================================

    SECRET_KEY: str = Field(
        ...,
        description="Secret key used to sign JWT tokens.",
    )

    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # =====================================================
    # Database
    # =====================================================

    POSTGRES_HOST: str

    POSTGRES_PORT: int

    POSTGRES_DB: str

    POSTGRES_USER: str

    POSTGRES_PASSWORD: str

    # =====================================================
    # Redis
    # =====================================================

    REDIS_HOST: str

    REDIS_PORT: int

    # =====================================================
    # Twilio
    # =====================================================

    TWILIO_ACCOUNT_SID: str = ""

    TWILIO_AUTH_TOKEN: str = ""

    TWILIO_PHONE_NUMBER: str = ""

    # =====================================================
    # Email
    # =====================================================

    SMTP_HOST: str = ""

    SMTP_PORT: int = 587

    SMTP_USERNAME: str = ""

    SMTP_PASSWORD: str = ""

    SMTP_FROM_EMAIL: str = ""

    # =====================================================
    # URLs
    # =====================================================

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )

    @property
    def REDIS_URL(self) -> str:
        return (
            f"redis://"
            f"{self.REDIS_HOST}:"
            f"{self.REDIS_PORT}"
        )


@lru_cache
def get_settings() -> Settings:
    """
    Cached settings instance.
    """
    return Settings()


settings = get_settings()