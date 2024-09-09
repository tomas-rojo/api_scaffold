from exceptions.item_not_found import ItemNotFound
from ports.abstract_repository import AbstractRepository


class ListRepository(AbstractRepository):
    def __init__(self) -> None:
        self._collection: list[str] = []

    def add(self, id: str) -> None:
        self._collection.append(id)

    def get(self, id: str) -> str:
        try:
            return [item for item in self._collection if item == id][0]
        except Exception as e:
            raise ItemNotFound(id) from e
