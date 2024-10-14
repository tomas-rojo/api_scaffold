from adapters.sql_repository import SQLRepository
from ports.abstract_repository import AbstractRepository
from sqlalchemy import URL, Engine, create_engine

from config.dependency import Dependency
from config.instances.base_config import BaseConfig
from config.settings.postgres_settings import PostgresSettings


class DevelopmentConfig(BaseConfig):
    def __init__(self) -> None:
        Dependency.add_singleton("api_url", "integration.example.org")
        Dependency.add_singleton_factory(AbstractRepository, lambda: SQLRepository(self.engine))

    @property
    def url(self) -> URL:
        return PostgresSettings().get_engine_url()

    @property
    def engine(self) -> Engine:
        return create_engine(self.url, pool_size=10)
