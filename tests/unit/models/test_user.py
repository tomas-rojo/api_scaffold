import uuid
from models.user import User


def test_can_instantiate_user() -> None:
    user_id = uuid.UUID("3c9c40e2b2ed4f64a675178465a7c28a")
    user = User(id=user_id, email="user@example.com", is_active=True)
    assert user.id == user_id
    assert user.email == "user@example.com"
    assert user.is_active is True