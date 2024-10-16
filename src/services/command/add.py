from config.dependency import Dependency
from models.user import User
from ports.abstract_repository import AbstractRepository


def add_element(user: User) -> None:
    repository = Dependency.get(AbstractRepository)
    return repository.add(user)
