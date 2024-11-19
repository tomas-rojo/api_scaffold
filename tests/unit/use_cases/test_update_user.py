import pytest
from models.user import User
from services.command.add_user import add_user
from services.query.get_user import get_user
from use_cases.add_user import AddUserUseCase
from use_cases.update_user import UpdateUserUseCase


def test_can_update_user(user: User) -> None:
    add_user(user)
    updated_user = User(id=user.id, is_active=False, email=user.email)
    UpdateUserUseCase(updated_user).execute()
    assert get_user(updated_user.id.hex) == updated_user

def test_raises_user_not_found_when_updating_non_existent_user(user: User) -> None:
    with pytest.raises(UpdateUserUseCase.NotFound):
        UpdateUserUseCase(user=user).execute()

def test_raises_user_email_already_exists_when_updating_user(user: User) -> None:
    AddUserUseCase(user).execute()

    # Add another user with a different ID but the same email
    conflicting_user = User(email="conflicting_user@example.com", is_active=True)
    AddUserUseCase(conflicting_user).execute()

    # Update the initial user to have the conflicting email
    updated_user = User(id=user.id, email="conflicting_user@example.com", is_active=False)

    with pytest.raises(UpdateUserUseCase.UserEmailAlreadyExists):
        UpdateUserUseCase(user=updated_user).execute()