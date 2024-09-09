from config.container import container
from ports.abstract_repository import AbstractRepository


def get_element(id: str) -> str:
    repository: AbstractRepository = container.repository
    return repository.get(id)
