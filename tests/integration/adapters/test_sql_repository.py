from ports.abstract_repository import AbstractRepository


def test_config_repo_2(repository: AbstractRepository) -> None:
    repository.add("1")
    result = repository.get("1")
    assert "1" == result
