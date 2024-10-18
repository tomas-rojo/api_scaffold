from sqlalchemy import create_engine

from shared.alembic import AlembicEnv


# Run migrations.
engine = create_engine('sqlite:///:memory:')
AlembicEnv(engine).execute()
