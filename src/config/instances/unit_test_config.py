from adapters.dict_repository import DictRepository
from ports.abstract_repository import AbstractRepository

from config.dependency import Dependency
from config.instances.base_config import BaseConfig


class UnitTestConfig(BaseConfig):
    def __init__(self) -> None:
        Dependency.add_singleton(AbstractRepository, DictRepository())
