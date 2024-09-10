from adapters.sql_repository import Base
from config.settings.postgres_settings import PostgresSettings
from shared.alembic import AlembicEnv
from sqlalchemy import create_engine

engine_url = PostgresSettings().get_engine_url()
engine = create_engine(engine_url, pool_pre_ping=True)
AlembicEnv(engine=engine, target_metadata=Base.metadata).execute()
