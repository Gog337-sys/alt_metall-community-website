from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ENV_FILE = PROJECT_ROOT / ".env"

class Setting(BaseSettings):
    app_name: str = "Alt_metall-community-website"
    app_version: str = "0.1.0"
    debug: bool = True
    hosts: str = "127.0.0.1"
    port: int = 8000
    database_url: str = "sqlite:///./database.db"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expere_minutes: int = 30 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings() -> Setting:
    return Setting()