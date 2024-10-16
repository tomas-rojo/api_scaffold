import pytest
from services.command.add import add_element
from use_cases.get_index import IndexUseCase


def test_can_get_index() -> None:
    add_element("1")
    assert IndexUseCase("1").execute() == "1"

def test_can_get_index_raise_exception_if_number_not_found() -> None:
    with pytest.raises(IndexUseCase.NotFound):
        IndexUseCase("2").execute()