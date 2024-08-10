from adapters.list_repository import ListRepository

from config.instances.base_config import BaseConfig


class IntegrationTestConfig(BaseConfig):
    api_url = "integration.example.org"
    repository = ListRepository()
