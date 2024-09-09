from __future__ import annotations

from ports.abstract_repository import AbstractRepository

from config.environment import Environment
from config.instances.base_config import BaseConfig
from config.settings.web_settings import WebSettings


class Container:
    @property
    def config(self) -> BaseConfig:
        return Environment.bootstrap()

    @property
    def repository(self) -> AbstractRepository:
        return self.config.repository

    @property
    def api_url(self) -> str:
        return self.config.api_url

    @property
    def web_settings(self) -> WebSettings:
        return self.config.web_settings

    def as_settings(self) -> dict[str, str]:
        settings = {}
        for name in dir(self):
            if isinstance(getattr(type(self), name, None), property) and name != "config":
                settings[name] = getattr(self, name)
        return settings


container = Container()
