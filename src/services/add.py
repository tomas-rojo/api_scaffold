from config.container import container
from ports.abstract_repository import AbstractRepository


def add_element(id: str) -> None:
    repository: AbstractRepository = container.repository
    return repository.add(id)
