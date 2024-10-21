import pytest
from models.user import User
from services.command.add_user import add_user 
from use_cases.get_user import GetUserUseCase


def test_can_get_user(user: User) -> None:
    add_user(user)
    assert GetUserUseCase(user.id).execute() == user

def test_get_user_raise_exception_if_userr_not_found() -> None:
    with pytest.raises(GetUserUseCase.NotFound):
        GetUserUseCase("invalid-id").execute()