from abc import ABC, abstractmethod
from uuid import UUID

from exceptions.invalid_user_id import InvalidUserId
from models.user import User


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        raise NotImplementedError

    def get(self, user_id: str) -> User:
        try:
            user_uuid = UUID(user_id)
        except ValueError:
            raise InvalidUserId(user_id) from None
        return self._get(user_uuid)

    @abstractmethod
    def _get(self, user_uuid: UUID) -> User:
        raise NotImplementedError

    def remove(self, user_id: str) -> None:
        try:
            user_uuid = UUID(user_id)
        except ValueError:
            raise InvalidUserId(user_id) from None
        return self._remove(user_uuid)

    @abstractmethod
    def _remove(self, user_uuid: UUID) -> None:
        raise NotImplementedError
