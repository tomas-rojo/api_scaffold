from os import environ
from typing import Callable

from config.instances.base_config import BaseConfig
from config.instances.development_config import DevelopmentConfig
from config.instances.integration_test_config import IntegrationTestConfig
from config.instances.production_config import ProductionConfig
from config.instances.unit_test_config import UnitTestConfig


class Environment:
    environments: dict[str, Callable[[], BaseConfig]] = {
        "unit-test": UnitTestConfig,
        "integration": IntegrationTestConfig,
        "development": DevelopmentConfig,
        "production": ProductionConfig,
    }

    @staticmethod
    def bootstrap() -> BaseConfig:
        """Bootstraps the DI configuration."""
        environment_name = Environment.get_environment_name()
        return Environment.create_config(environment_name)

    @staticmethod
    def get_environment_name() -> str:
        environment_name = environ.get("APP_ENVIRONMENT", None)
        if environment_name:
            return environment_name
        else:
            raise SystemError("Environment variable APP_ENVIRONMENT is not set")

    @staticmethod
    def create_config(environment_name: str) -> BaseConfig:
        try:
            return Environment.environments[environment_name]()
        except KeyError:
            raise SystemError(f"Invalid value '{environment_name}' for environment variable APP_ENVIRONMENT") from None
