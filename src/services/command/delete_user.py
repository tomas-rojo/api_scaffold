from config.dependency import Dependency
from models.user import User
from ports.abstract_repository import AbstractRepository


def delete_user(user: User) -> None:
    repository = Dependency.get(AbstractRepository)
    return repository.add(user)