import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SQLITE_URL: str = os.getenv("SQLITE_URL", "sqlite:///./ecom.db")

settings = Settings()