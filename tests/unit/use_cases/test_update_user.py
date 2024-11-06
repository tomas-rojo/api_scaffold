import pytest
from models.user import User
from services.command.add_user import add_user
from services.query.get_user import get_user
from use_cases.update_user import UpdateUserUseCase


def test_can_update_user(user: User) -> None:
    add_user(user)
    updated_user = User(id=user.id, is_active=False, email=user.email)
    UpdateUserUseCase(updated_user).execute()
    assert get_user(updated_user.id.hex) == updated_user

def test_raises_user_not_found_when_updating_non_existent_user(user: User) -> None:
    with pytest.raises(UpdateUserUseCase.NotFound):
        UpdateUserUseCase(user=user).execute()