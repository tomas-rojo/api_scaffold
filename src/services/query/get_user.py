from config.dependency import Dependency
from ports.abstract_repository import AbstractRepository


def get_user(id: str) -> str:
    repository = Dependency.get(AbstractRepository)
    return repository.get(id)
