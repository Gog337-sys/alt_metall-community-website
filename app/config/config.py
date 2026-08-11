from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

class Setting(BaseSettings):
    app_name: str = "Alt_metall-community-website"
    app_version: str = "0.1.0"
    debug: bool = True

    hosts: str = "127.0.0.1"
    port: int = 8000

    database_url: str = "sqlite:///./database.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

@lru_cache
def get_settings() -> Setting:
    return Setting()