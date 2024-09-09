from adapters.dict_repository import DictRepository

from config.instances.base_config import BaseConfig


class UnitTestConfig(BaseConfig):
    repository = DictRepository()
