import pytest
from models.user import User
from services.query.get_user import get_user
from use_cases.add_user import AddUserUseCase
from use_cases.get_user import GetUserUseCase


def test_can_add_user(user: User) -> None:
    AddUserUseCase(user).execute()
    assert get_user(user.id.hex) == user

def test_get_user_raise_exception_if_user_not_found() -> None:
    with pytest.raises(GetUserUseCase.NotFound):
        GetUserUseCase("3c9c40e2b2ed4f64a675178465a7c28a").execute()