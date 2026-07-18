"""Application settings and configuration."""

from typing import Any, Dict, List
from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import Field
import json


class Settings(BaseSettings):
    """Application configuration settings."""

    # ==========================
    # Application
    # ==========================
    APP_NAME: str = Field(default="GLOBAL X SPARK AI", description="Application name")
    APP_VERSION: str = Field(default="1.0.0", description="Application version")
    DEBUG: bool = Field(default=False, description="Debug mode")
    ENVIRONMENT: str = Field(default="production", description="Environment")

    # ==========================
    # Security
    # ==========================
    SECRET_KEY: str = Field(
        default="change-me-in-production",
        description="Secret key for JWT encoding",
    )
    ALGORITHM: str = Field(default="HS256", description="JWT algorithm")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=30, description="Access token expiration time in minutes"
    )
    REFRESH_TOKEN_EXPIRE_DAYS: int = Field(
        default=7, description="Refresh token expiration time in days"
    )

    # ==========================
    # Database
    # ==========================
    DATABASE_URL: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/spark_ai",
        description="PostgreSQL database URL",
    )
    DATABASE_ECHO: bool = Field(
        default=False, description="Echo SQL statements"
    )
    DATABASE_POOL_SIZE: int = Field(default=20, description="Database connection pool size")
    DATABASE_MAX_OVERFLOW: int = Field(
        default=10, description="Maximum overflow connections"
    )

    # ==========================
    # Redis
    # ==========================
    REDIS_URL: str = Field(
        default="redis://localhost:6379/0", description="Redis URL"
    )
    REDIS_CACHE_TTL: int = Field(
        default=3600, description="Cache TTL in seconds"
    )

    # ==========================
    # API
    # ==========================
    API_V1_STR: str = Field(default="/api/v1", description="API v1 prefix")
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        description="CORS allowed origins",
    )
    ROOT_PATH: str = Field(default="", description="Root path for API")

    # ==========================
    # Logging
    # ==========================
    LOG_LEVEL: str = Field(default="INFO", description="Logging level")
    LOG_FORMAT: str = Field(default="json", description="Log format (json or text)")

    # ==========================
    # AI Providers
    # ==========================
    OPENAI_API_KEY: str = Field(default="", description="OpenAI API key")
    GOOGLE_API_KEY: str = Field(default="", description="Google API key")
    ANTHROPIC_API_KEY: str = Field(default="", description="Anthropic API key")

    # ==========================
    # Email
    # ==========================
    SMTP_SERVER: str = Field(default="smtp.gmail.com", description="SMTP server")
    SMTP_PORT: int = Field(default=587, description="SMTP port")
    SMTP_USER: str = Field(default="", description="SMTP user")
    SMTP_PASSWORD: str = Field(default="", description="SMTP password")
    SMTP_FROM: str = Field(
        default="noreply@globalxsparkai.com", description="Email from address"
    )

    # ==========================
    # Rate Limiting
    # ==========================
    RATE_LIMIT_ENABLED: bool = Field(
        default=True, description="Enable rate limiting"
    )
    RATE_LIMIT_REQUESTS: int = Field(
        default=100, description="Requests per rate limit window"
    )
    RATE_LIMIT_WINDOW: int = Field(
        default=60, description="Rate limit window in seconds"
    )

    # ==========================
    # Feature Flags
    # ==========================
    FEATURE_AUTH_ENABLED: bool = Field(default=True, description="Enable authentication")
    FEATURE_OAUTH_ENABLED: bool = Field(default=False, description="Enable OAuth")
    FEATURE_2FA_ENABLED: bool = Field(default=False, description="Enable 2FA")

    class Config:
        """Pydantic config."""
        env_file = ".env"
        case_sensitive = True
        extra = "allow"


@lru_cache()
def get_settings() -> Settings:
    """Get cached application settings.

    Returns:
        Settings: Application configuration
    """
    return Settings()
