from sqlalchemy import create_engine, text

from shared.alembic import AlembicEnv


# Run migrations.
engine = create_engine('sqlite:///:memory:')
AlembicEnv(engine).execute()

# Try to INSERT and SELECT into the table that ought to have been
# created by the migrations to test if the migrations worked.
with engine.connect() as connection:
    connection.execute(text("INSERT INTO test VALUES (42)"))
    result = connection.execute(text("SELECT * FROM test"))
    assert result.scalar() == 42
