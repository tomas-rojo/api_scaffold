import pytest
from exceptions.user_not_found import UserNotFound
from models.user import User
from ports.abstract_repository import AbstractRepository


def test_config_repo_2(repository: AbstractRepository, user: User) -> None:
    repository.add(user)
    result = repository.get(user.id)
    assert user == result


def test_repository_raises_exception_when_user_not_found(repository: AbstractRepository) -> None:
    with pytest.raises(UserNotFound):
        repository.get("invalid-id")