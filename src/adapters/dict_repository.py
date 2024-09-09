from exceptions.item_not_found import ItemNotFound
from ports.abstract_repository import AbstractRepository


class DictRepository(AbstractRepository):
    def __init__(self) -> None:
        self._collection: dict[str, str] = {}

    def add(self, id: str) -> None:
        self._collection[id] = id

    def get(self, id: str) -> str:
        try:
            return self._collection[id]
        except KeyError as e:
            raise ItemNotFound(id) from e
