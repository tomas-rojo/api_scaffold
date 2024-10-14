import os

import sqlalchemy
from pydantic import BaseModel, SecretStr


class PostgresSettings(BaseModel):
    host: str = os.environ.get("PG_HOST", "127.0.0.1")
    port: int = 5432
    username: str = str(os.environ.get("PG_USERNAME", "postgres"))
    password: SecretStr = SecretStr(os.environ.get("PG_PASSWORD", "postgres"))
    database: str = str(os.environ.get("PG_DATABASE", "postgres"))

    def get_engine_url(self) -> sqlalchemy.URL:
        return sqlalchemy.URL.create(
            drivername="postgresql+psycopg2",
            username=self.username,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.database,
        )
