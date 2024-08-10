from services.get_status import get_status


def test_status() -> None:
    assert get_status() == "example.org"
