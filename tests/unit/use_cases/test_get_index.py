from use_cases.get_index import IndexUseCase


def test_can_get_index() -> None:
    assert IndexUseCase().execute() == "1"