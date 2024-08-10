from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, id: str) -> str:
        raise NotImplementedError
