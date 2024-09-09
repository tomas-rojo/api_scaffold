from services.query.get_status import get_status


def test_status2() -> None:
    assert get_status() == "integration.example.org"
