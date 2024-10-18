import os
from pathlib import Path

import alembic.config
from pytest import raises
from sqlalchemy import Column, String, Table, create_engine
from sqlalchemy.orm import registry

from shared.alembic import AlembicEnv, AlembicUpgrade



def test_alembic_env_can_perform_alembic_upgrade() -> None:
    pwd = os.getcwd()
    os.chdir(Path(__file__).parent / "alembic-env-test")
    try:
        # Run alembic to perform a migration. The actual assertion for the
        # migration can be found in `migrations_for_testing/env.py`.
        alembic.config.main(argv=["upgrade", "head"])
    finally:
        os.chdir(pwd)


def test_alembic_env_does_not_support_offline_mode() -> None:
    pwd = os.getcwd()
    os.chdir(Path(__file__).parent / "alembic-env-test")
    try:
        with raises(RuntimeError, match="Offline mode is not supported"):
            alembic.config.main(argv=["upgrade", "head", "--sql"])
    finally:
        os.chdir(pwd)


def test_alembic_upgrade_performs_upgrade_when_executed() -> None:
    with raises(NotImplementedError, match=r"upgrade\(\) is called"):
        AlembicUpgrade(Path(__file__).parent / "alembic-upgrade-test").execute()


def test_when_using_metadata_only_tables_from_metadata_will_be_managed_by_alembic() -> None:
    mapper_registry = registry()
    metadata = mapper_registry.metadata
    Table("test_table_1", metadata, Column("id", String, primary_key=True))
    Table("test_table_2", metadata, Column("id", String, primary_key=True))
    engine = create_engine('sqlite:///:memory:')
    alembic_env = AlembicEnv(engine=engine, target_metadata=metadata)

    include_object_function = alembic_env._make_include_object_function()
    assert include_object_function(None, "test_table_1", "table", True, None) is True
    assert include_object_function(None, "test_table_1", "table", True, None) is True
    assert include_object_function(None, "other_table", "table", True, None) is False
