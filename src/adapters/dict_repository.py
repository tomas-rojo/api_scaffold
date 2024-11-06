import uuid
from uuid import UUID

from exceptions.user_not_found import UserNotFound
from models.user import User
from ports.abstract_repository import AbstractRepository


class DictRepository(AbstractRepository):
    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}

    def add(self, user: User) -> None:
        self._users[user.id] = user

    def _get(self, id: uuid.UUID) -> User:
        try:
            return self._users[id]
        except KeyError as e:
            raise UserNotFound(id.hex) from e

    def _remove(self, id: uuid.UUID) -> None:
        try:
            del self._users[id]
        except KeyError as e:
            raise UserNotFound(id.hex) from e

    def update(self, user: User) -> None:
        _user = self._get(user.id)
        self._users[user.id] = _user
