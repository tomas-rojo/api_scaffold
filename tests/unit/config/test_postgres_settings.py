from pydantic import SecretStr
import pytest
from config.settings.postgres_settings import PostgresSettings  # Replace with the actual module name

def test_postgres_settings_init() -> None:
    settings = PostgresSettings(
        host="localhost",
        port=5432,
        database="mydatabase",
        username="myuser",
        password=SecretStr("mypassword")
    )
    assert settings.host == "localhost"
    assert settings.port == 5432
    assert settings.database == "mydatabase"
    assert settings.username == "myuser"
    assert settings.password.get_secret_value() == "mypassword"
