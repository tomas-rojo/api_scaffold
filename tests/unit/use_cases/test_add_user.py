import pytest
from models.user import User
from services.query.get_user import get_user
from use_cases.add_user import AddUserUseCase
from use_cases.get_user import GetUserUseCase


def test_can_add_user(user: User) -> None:
    AddUserUseCase(user).execute()
    assert get_user(user.id.hex) == user

def test_add_user_raise_exception_if_user_not_found(user: User) -> None:
    AddUserUseCase(user).execute()
    with pytest.raises(AddUserUseCase.UserEmailAlreadyExists, match=f"User email {user.email} already exists"):
            AddUserUseCase(user).execute()
