import os
from collections.abc import Generator

from config.environment import Environment
from pytest import fixture


@fixture(autouse=True, scope="module")
def setup() -> Generator[None, None, None]:
    os.environ["APP_ENVIRONMENT"] = "integration"
    Environment.bootstrap()
    yield
    return None
