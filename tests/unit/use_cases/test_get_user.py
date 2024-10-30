import pytest
from models.user import User
from services.command.add_user import add_user 
from use_cases.get_user import GetUserUseCase


def test_can_get_user(user: User) -> None:
    add_user(user)
    assert GetUserUseCase(str(user.id)).execute() == user

def test_get_user_raise_exception_if_user_not_found() -> None:
    with pytest.raises(GetUserUseCase.NotFound):
        GetUserUseCase("3c9c40e2b2ed4f64a675178465a7c28a").execute()

def test_get_user_raise_exception_if_user_id_is_invalid() -> None:
    with pytest.raises(GetUserUseCase.InvalidId):
        GetUserUseCase("invalid-id").execute()
