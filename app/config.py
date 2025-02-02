from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False
    postgres_user: str
    postgres_password: str
    postgres_db: str

    class Config:
        env_file = ".env"

settings = Settings()
