import logging
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger('uvicorn')


class Settings(BaseSettings):
    environment: str = 'dev'
    testing: bool = 0


@lru_cache()    # This catches the configuration
async def get_settings() -> BaseSettings:
    log.info('Loading config settings from the environment...')
    return Settings()
