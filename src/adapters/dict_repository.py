from exceptions.user_not_found import UserNotFound
from models.user import User
from ports.abstract_repository import AbstractRepository


class DictRepository(AbstractRepository):
    def __init__(self) -> None:
        self._users: dict[str, User] = {}

    def add(self, user: User) -> None:
        self._users[user.id] = user

    def get(self, id: str) -> str:
        try:
            return self._users[id]
        except KeyError as e:
            raise UserNotFound(id) from e

    def remove(self, id: str) -> str:
        try:
            del self._users[id]
        except KeyError as e:
            raise UserNotFound(id) from e