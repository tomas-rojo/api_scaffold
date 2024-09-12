from models.user import User


def test_can_instantiate_user() -> None:
    user = User(id="abc123", email="user@example.com", is_active=True)
    assert user.id == "abc123"
    assert user.email == "user@example.com"
    assert user.is_active is True