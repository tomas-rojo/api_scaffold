from config.dependency import Dependency
from ports.abstract_repository import AbstractRepository


def remove_user(id: str) -> None:
    repository = Dependency.get(AbstractRepository)
    repository.remove(id)
