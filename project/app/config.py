import logging

from pydantic import BaseSettings

log = logging.getLogger('uvicorn')


class DatabaseSettings(BaseSettings):
    database_name: str
    database_user: str
    database_password: str
    database_host: str
    database_port: str

class Settings(BaseSettings):
    environment: str = 'dev'
    testing: bool = 0
    secret_key: str


async def get_settings() -> BaseSettings:
    log.info('Loading config settings from the environment...')
    return Settings()
