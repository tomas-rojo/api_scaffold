from config.dependency import Dependency
from models.user import User
from ports.abstract_repository import AbstractRepository
from pytest import fixture


@fixture
def repository() -> AbstractRepository:
    repository = Dependency.get(AbstractRepository)
    return repository

@fixture
def user() -> User:
    return User(
        email="test@example.com",
        is_active=True
    )