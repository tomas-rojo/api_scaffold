from config.container import container
from ports.abstract_repository import AbstractRepository
from pytest import fixture


@fixture
def repository() -> AbstractRepository:
    repository: AbstractRepository = container.repository
    return repository
