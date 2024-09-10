from dataclasses import dataclass

from exceptions.item_not_found import ItemNotFound
from services.query.get import get_element
from shared.use_cases import QueryUseCase, UseCaseException


@dataclass
class IndexUseCase(QueryUseCase[str]):
    number: str

    class NotFound(UseCaseException):
        message_fmt = "No result found for {number}"
        error_code = 404

    def _execute(self) -> str:
        try:
            return get_element(id=self.number)
        except ItemNotFound:
            raise self.NotFound(number=self.number) from None
