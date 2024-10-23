from config.dependency import Dependency
from models.user import User
from ports.abstract_repository import AbstractRepository


def get_user(id: str) -> User:
    repository = Dependency.get(AbstractRepository)
    return repository.get(id)
