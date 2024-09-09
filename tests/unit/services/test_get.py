from services.command.add import add_element
from services.query.get import get_element


def test_service_can_get_element() -> None:
    add_element("1")
    x = get_element("1")
    assert x == "1"
