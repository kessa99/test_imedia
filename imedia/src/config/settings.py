"""
configuration des variables d'environnement
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pydantic import Field, model_validator
from urllib.parse import quote_plus

class Settings(BaseSettings):
    """
    configuration pour la recuperation des informations du .env
    """
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env", env_file_encoding="utf-8")

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DATABASE_URL: str = ""

    @model_validator(mode="after")
    def build_database_url(self) -> "Settings":
        if not self.DATABASE_URL:
            self.DATABASE_URL = (
                f"postgresql://{self.DB_USER}:{quote_plus(self.DB_PASSWORD)}"
                f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
            )
        return self

settings = Settings()