import os
from collections.abc import Generator

from config.environment import Environment
from pytest import fixture


@fixture(autouse=True)
def setup() -> Generator[None, None, None]:
    os.environ["APP_ENVIRONMENT"] = "integration"
    Environment.bootstrap()
    yield
    Environment.teardown()
