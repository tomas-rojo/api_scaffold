import pytest
from exceptions.user_not_found import UserNotFound
from models.user import User
from services.command.add_user import add_user 
from services.query.get_user import get_user
from use_cases.remove_user import RemoveUserUseCase


def test_can_remove_user(user: User) -> None:
    add_user(user)
    _user = get_user(user.id.hex)

    # User exists, now we can proceed to remove it
    assert user == _user

    RemoveUserUseCase(user.id.hex).execute()

    with pytest.raises(UserNotFound):
        get_user(user.id.hex)


def test_remove_user_raise_exception_if_user_not_found() -> None:
    with pytest.raises(RemoveUserUseCase.NotFound):
        RemoveUserUseCase("3c9c40e2b2ed4f64a675178465a7c28a").execute()

def test_remove_user_raise_exception_if_user_id_is_invalid() -> None:
    with pytest.raises(RemoveUserUseCase.InvalidId):
        RemoveUserUseCase("invalid-id").execute()
