from adapters.dict_repository import DictRepository
from config.instances.base_config import BaseConfig
from ports.abstract_repository import AbstractRepository

from config.dependency import Dependency


class UnitTestConfig(BaseConfig):
    def __init__(self) -> None:
        Dependency.add_singleton("api_url", "unit.example.org")
        Dependency.add_singleton_factory(AbstractRepository, lambda: DictRepository())
