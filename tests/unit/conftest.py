from collections.abc import Generator
import os

from config.environment import Environment
from pytest import fixture
from starlette.testclient import TestClient
from web_app.api import api



@fixture(autouse=True, scope="module")
def setup() -> Generator[None, None, None]:
    os.environ["APP_ENVIRONMENT"] = "unit-test"
    Environment.bootstrap()
    yield
    return None

@fixture
def client() -> TestClient:
    return TestClient(api)