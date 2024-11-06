import pytest
from exceptions.invalid_user_id import InvalidUserId
from exceptions.user_not_found import UserNotFound
from models.user import User
from ports.abstract_repository import AbstractRepository


def test_config_repo_2(repository: AbstractRepository, user: User) -> None:
    repository.add(user)
    result = repository.get(user.id.hex)
    assert user == result


def test_repository_get_user_raises_exception_when_user_not_found(repository: AbstractRepository) -> None:
    with pytest.raises(InvalidUserId):
        repository.get("invalid-id")

def test_repository_remove_user_raises_exception_when_user_not_found(repository: AbstractRepository) -> None:
    with pytest.raises(UserNotFound):
        repository.remove("3c9c40e2b2ed4f64a675178465a7c28a")

def test_repository_updates_user(repository: AbstractRepository, user: User) -> None:
    repository.add(user)
    updated_user = User(id=user.id, email=user.email, is_active=False)
    repository.update(updated_user)
    result = repository.get(updated_user.id.hex)
    assert updated_user.is_active is False