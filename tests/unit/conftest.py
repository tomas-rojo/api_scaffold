from collections.abc import Generator
import os

from flask.testing import FlaskClient

from config.environment import Environment
from pytest import fixture
from starlette.testclient import TestClient
from web_app.api import api


@fixture(autouse=True)
def setup() -> Generator[None, None, None]:
    os.environ["APP_ENVIRONMENT"] = "unit-test"
    Environment.bootstrap()
    yield
    Environment.teardown()

@fixture
def client() -> TestClient:
    return TestClient(api)

# @fixture
# def flask_client() -> FlaskClient:
#     return app.test_client()