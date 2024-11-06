from dataclasses import dataclass

from exceptions.user_email_already_exists import EmailAlreadyExists
from exceptions.user_not_found import UserNotFound
from models.user import User
from services.command.update_user import update_user
from shared.use_cases import CommandUseCase, UseCaseException


@dataclass
class UpdateUserUseCase(CommandUseCase):
    user: User

    class NotFound(UseCaseException):
        message_fmt = "No user found with ID {user_id}"
        error_code = 404

    class UserEmailAlreadyExists(UseCaseException):
        message_fmt = "User email {user_email} already exists"
        error_code = 404

    def _execute(self) -> None:
        try:
            update_user(self.user)
        except EmailAlreadyExists:
            raise self.UserEmailAlreadyExists(user_email=self.user.email) from None
        except UserNotFound:
            raise self.NotFound(user_id=self.user.id.hex) from None
