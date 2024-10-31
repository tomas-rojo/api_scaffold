import sys

from adapters.sql_repository import Base, SQLRepository
from config.dependency import Dependency
from config.environment import Environment
from ports.abstract_repository import AbstractRepository
from shared.alembic import AlembicEnv

try:
    Environment.bootstrap()
    repository = Dependency.get(AbstractRepository)
    if isinstance(repository, SQLRepository):
        AlembicEnv(engine=repository._engine, target_metadata=Base.metadata).execute()
except Exception as e:  # noqa
    print(f"Unable to bootstrap environment: {str(e)}", file=sys.stderr)
    sys.exit(1)
