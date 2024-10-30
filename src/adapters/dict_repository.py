from uuid import UUID
import uuid
from exceptions.invalid_user_id import InvalidUserId
from exceptions.user_not_found import UserNotFound
from models.user import User
from ports.abstract_repository import AbstractRepository


class DictRepository(AbstractRepository):
    def __init__(self) -> None:
        self._users: dict[UUID, User] = {}

    def add(self, user: User) -> None:
        self._users[user.id] = user

    def get(self, id: str) -> User:
        try:
            uuid_user_id = uuid.UUID(id)
        except ValueError:
            raise InvalidUserId(id) from None
        try:
            return self._users[uuid_user_id]
        except KeyError as e:
            raise UserNotFound(id) from e

    def remove(self, id: str) -> None:
        try:
            uuid_user_id = uuid.UUID(id)
        except ValueError:
            raise InvalidUserId(id) from None
        try:
            del self._users[uuid_user_id]
        except KeyError as e:
            raise UserNotFound(id) from e
