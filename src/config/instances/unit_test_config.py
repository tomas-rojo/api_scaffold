from adapters.dict_repository import DictRepository

from config.dependency import Dependency
from config.instances.base_config import BaseConfig
from ports.abstract_repository import AbstractRepository


class UnitTestConfig(BaseConfig):
    def __init__(self):
        Dependency.add_singleton("api_url", "example.org")
        Dependency.add_singleton_factory(AbstractRepository, lambda: DictRepository())
