from config.dependency import Dependency
from ports.abstract_repository import AbstractRepository


def add_element(id: str) -> None:
    repository = Dependency.get(AbstractRepository)
    return repository.add(id)
