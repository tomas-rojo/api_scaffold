from config.dependency import Dependency
from ports.abstract_repository import AbstractRepository
from pytest import fixture


@fixture
def repository() -> AbstractRepository:
    repository = Dependency.get(AbstractRepository)
    return repository
