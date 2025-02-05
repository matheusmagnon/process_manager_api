"""
Application configuration settings loaded from environment variables.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Main application settings configuration.

    Attributes:
        database_url: Complete database connection URL.
        secret_key: Secret key for security operations.
        debug: Debug mode flag (default False).
        postgres_user: PostgreSQL database username.
        postgres_password: PostgreSQL database password.
        postgres_db: PostgreSQL database name.
    """

    database_url: str
    secret_key: str
    debug: bool = False
    postgres_user: str
    postgres_password: str
    postgres_db: str

    class Config: # pylint: disable=too-few-public-methods
        """Pydantic configuration for settings loading."""
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
