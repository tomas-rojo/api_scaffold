from abc import ABC, abstractmethod

from models.user import User


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, user_id: str) -> User:
        raise NotImplementedError

    @abstractmethod
    def remove(self, user_id: str) -> None:
        raise NotImplementedError