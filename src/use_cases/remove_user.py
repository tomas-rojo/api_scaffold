from dataclasses import dataclass

from exceptions.invalid_user_id import InvalidUserId
from exceptions.user_not_found import UserNotFound
from services.command.remove_user import remove_user
from services.query.get_user import get_user
from shared.use_cases import CommandUseCase, UseCaseException


@dataclass
class RemoveUserUseCase(CommandUseCase):
    user_id: str

    class NotFound(UseCaseException):
        message_fmt = "No user found with ID {user_id}"
        error_code = 404

    class InvalidId(UseCaseException):
        message_fmt = "User ID: {user_id} is invalid"
        error_code = 404

    def _execute(self) -> None:
        try:
            get_user(id=self.user_id)
            remove_user(self.user_id)
        except UserNotFound:
            raise self.NotFound(user_id=self.user_id) from None
        except InvalidUserId:
            raise self.InvalidId(user_id=self.user_id) from None
