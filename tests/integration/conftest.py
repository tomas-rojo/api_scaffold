import os
from collections.abc import Generator

from adapters.sql_repository import SQLRepository
from config.dependency import Dependency
from config.environment import Environment
from pytest import fixture

from ports.abstract_repository import AbstractRepository


@fixture(autouse=True)
def setup() -> Generator[None, None, None]:
    os.environ["APP_ENVIRONMENT"] = "integration"
    Environment.bootstrap()
    repository = Dependency.get(AbstractRepository)
    assert isinstance(repository, SQLRepository)
    repository.create_schema()
    yield
    repository.drop_schema()
    Environment.teardown()
