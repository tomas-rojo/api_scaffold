from ports.abstract_repository import AbstractRepository

from config.settings.web_settings import WebSettings


class BaseConfig:
    api_url = "example.org"
    repository: AbstractRepository
    web_settings = WebSettings()
