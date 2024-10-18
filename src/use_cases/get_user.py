from dataclasses import dataclass

from exceptions.item_not_found import ItemNotFound
from services.query.get_user import get_user
from shared.use_cases import QueryUseCase, UseCaseException


@dataclass
class GetUserUseCase(QueryUseCase[str]):
    user_id: str

    class NotFound(UseCaseException):
        message_fmt = "No user found with ID {user_id}"
        error_code = 404

    def _execute(self) -> str:
        try:
            return get_user(id=self.user_id)
        except ItemNotFound:
            raise self.NotFound(user_id=self.user_id) from None
