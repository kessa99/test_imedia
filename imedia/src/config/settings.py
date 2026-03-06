"""
configuration des variables d'environnement
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from pydantic import Field

class Settings(BaseSettings):
    """
    configuration pour la recuperation des informations du .env
    """
    model_config = SettingsConfigDict(env_file=Path(__file__).parent.parent / ".env", env_file_encoding="utf-8")

    DATABASE_URL: str = Field(..., env="DATABASE_URL")

settings = Settings()