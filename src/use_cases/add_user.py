from dataclasses import dataclass

from exceptions.user_email_already_exists import EmailAlreadyExists
from models.user import User
from services.command.add_user import add_user
from shared.use_cases import CommandUseCase, UseCaseException


@dataclass
class AddUserUseCase(CommandUseCase):
    user: User

    class UserEmailAlreadyExists(UseCaseException):
        message_fmt = "User email {user_email} already exists"
        error_code = 404

    def _execute(self) -> None:
        try:
            add_user(self.user)
        except EmailAlreadyExists:
            raise self.UserEmailAlreadyExists(user_email=self.user.email) from None
