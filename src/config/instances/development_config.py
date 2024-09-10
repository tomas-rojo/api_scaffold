from adapters.sql_repository import SQLRepository
from sqlalchemy import URL, Engine, create_engine

from config.instances.base_config import BaseConfig
from config.settings.postgres_settings import PostgresSettings


class DevelopmentConfig(BaseConfig):
    api_url = "integration.example.org"

    def __init__(self) -> None:
        self.repository = self.get_repository()

    @property
    def url(self) -> URL:
        return PostgresSettings().get_engine_url()

    @property
    def engine(self) -> Engine:
        return create_engine(self.url, pool_pre_ping=True)

    def get_repository(self) -> SQLRepository:
        return SQLRepository(self.engine)
