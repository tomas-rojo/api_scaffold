from collections.abc import Generator
import os

from flask.testing import FlaskClient

from adapters.sql_repository import SQLRepository
from config.dependency import Dependency
from config.environment import Environment
from pytest import fixture
from starlette.testclient import TestClient
from ports.abstract_repository import AbstractRepository
from web_app.api import api
from web_app.app import app


@fixture(autouse=True)
def setup() -> Generator[None, None, None]:
    os.environ["APP_ENVIRONMENT"] = "unit-test"
    Environment.bootstrap()
    repository = Dependency.get(AbstractRepository)
    assert isinstance(repository, SQLRepository)
    repository.create_schema()
    yield
    repository.drop_schema()
    Environment.teardown()

@fixture
def client() -> TestClient:
    return TestClient(api)

@fixture
def flask_client() -> FlaskClient:
    return app.test_client()