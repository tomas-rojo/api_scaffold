import pytest
from models.user import User
from services.query.get_user import get_user
from use_cases.add_user import AddUserUseCase


def test_can_add_user(user: User) -> None:
    AddUserUseCase(user).execute()
    assert get_user(user.id) == user

# def test_get_user_raise_exception_if_userr_not_found() -> None:
#     with pytest.raises(GetUserUseCase.NotFound):
#         GetUserUseCase("invalid-id").execute()