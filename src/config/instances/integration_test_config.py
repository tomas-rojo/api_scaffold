from adapters.dict_repository import DictRepository
from ports.abstract_repository import AbstractRepository

from config.dependency import Dependency
from config.instances.base_config import BaseConfig


class IntegrationTestConfig(BaseConfig):
    def __init__(self) -> None:
        Dependency.add_singleton("api_url", "integration.example.org")
        Dependency.add_singleton_factory(AbstractRepository, lambda: DictRepository())
