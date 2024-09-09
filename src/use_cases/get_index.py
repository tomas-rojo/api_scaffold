from dataclasses import dataclass
from services.query.get import get_element
from shared.use_cases import QueryUseCase, UseCaseException


@dataclass
class IndexUseCase(QueryUseCase):
    number: str

    class NotFound(UseCaseException):
        message_fmt = "No result found for {number}"
        error_code = 404

    def _execute(self) -> str:
        try:
            return get_element(self.number)
        except Exception:
            raise self.NotFound(number=self.number) from None
