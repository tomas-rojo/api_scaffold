import pytest
from exceptions.user_not_found import UserNotFound
from models.user import User
from services.command.add_user import add_user 
from services.query.get_user import get_user
from use_cases.remove_user import RemoveUserUseCase


def test_can_remove_user(user: User) -> None:
    add_user(user)
    _user = get_user(user.id)

    # User exists, now we can proceed to remove it
    assert user == _user

    RemoveUserUseCase(user.id).execute()

    with pytest.raises(UserNotFound):
        get_user(user.id)


def test_remove_user_raise_exception_if_user_not_found() -> None:
    with pytest.raises(RemoveUserUseCase.NotFound):
        RemoveUserUseCase("invalid-id").execute()