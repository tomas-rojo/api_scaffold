from adapters.list_repository import ListRepository

from config.instances.base_config import BaseConfig


from config.dependency import Dependency
from ports.abstract_repository import AbstractRepository


class IntegrationTestConfig(BaseConfig):
    def __init__(self):
        Dependency.add_singleton("api_url", "integration.example.org")
        Dependency.add_singleton_factory(AbstractRepository, lambda: ListRepository())
