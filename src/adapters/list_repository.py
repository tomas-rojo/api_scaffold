from ports.abstract_repository import AbstractRepository


class ListRepository(AbstractRepository):
    def __init__(self) -> None:
        self._collection: list[str] = []

    def add(self, id: str) -> None:
        self._collection.append(id)

    def get(self, id: str) -> str:
        return [item for item in self._collection if item == id][0]
