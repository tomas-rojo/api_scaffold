from pydantic import BaseModel, SecretStr


class PostgresSettings(BaseModel):
    host: str
    port: int
    database: str
    username: str
    password: SecretStr
    max_connections: int = 10
    max_idle_connections: int = 5
    timeout: int = 30
