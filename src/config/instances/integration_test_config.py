from adapters.dict_repository import DictRepository
from adapters.sql_repository import SQLRepository
from ports.abstract_repository import AbstractRepository
from sqlalchemy import Engine, StaticPool, create_engine

from config.dependency import Dependency
from config.instances.base_config import BaseConfig


class IntegrationTestConfig(BaseConfig):
    def __init__(self) -> None:
        Dependency.add_singleton_factory(AbstractRepository, lambda: SQLRepository(self.engine))

    @property
    def engine(self) -> Engine:
        return create_engine("sqlite://", poolclass=StaticPool, connect_args={"check_same_thread": False})
