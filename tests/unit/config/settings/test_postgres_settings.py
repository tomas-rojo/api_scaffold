import os
import pytest
from pydantic import SecretStr
from sqlalchemy.engine.url import URL

from config.settings.postgres_settings import PostgresSettings

@pytest.fixture
def default_settings() -> PostgresSettings:
    return PostgresSettings()

def test_postgres_default_settings(default_settings: PostgresSettings) -> None:
    assert default_settings.host == "127.0.0.1"
    assert default_settings.port == 5432
    assert default_settings.username == "postgres"
    assert default_settings.password == SecretStr("postgres")
    assert default_settings.database == "postgres"


def test_postgres_get_engine_url(default_settings: PostgresSettings) -> None:
    expected_url = URL.create(
        drivername="postgresql+psycopg2",
        username="postgres",
        password="postgres",
        host="127.0.0.1",
        port=5432,
        database="postgres",
    )

    engine_url = default_settings.get_engine_url()

    assert str(engine_url) == str(expected_url)
