from dataclasses import dataclass

from models.user import User
from services.command.add_user import add_user
from shared.use_cases import CommandUseCase, UseCaseException


@dataclass
class AddUserUseCase(CommandUseCase):
    user: User

    class NotFound(UseCaseException):
        message_fmt = "No user found with ID {user}"
        error_code = 404

    def _execute(self) -> None:
        add_user(self.user)

