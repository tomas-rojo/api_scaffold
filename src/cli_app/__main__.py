import sys
from pathlib import Path
from pprint import pprint

import click
import uvicorn
from adapters.sql_repository import SQLRepository

from config.environment import Environment
from shared.alembic import AlembicUpgrade

PROG_NAME = "testctl"


@click.group
def cli() -> None:
    """Test Provisioning System CLI"""
    pass


@cli.command()
def run() -> None:
    """Start the webserver process"""
    pass
    # web_settings = container.web_settings
    # if isinstance(container.repository, SQLRepository):
    #     script_location = Path(__file__).parent.parent / "migrations"
    #     AlembicUpgrade(script_location).execute()
    # uvicorn.run("web_app.api:api", port=web_settings.port, host=web_settings.host, reload=web_settings.debug)


@cli.command()
def config() -> None:
    """Show the running config"""
    return {"hello": "world"}


try:
    Environment.bootstrap()
    cli(prog_name=PROG_NAME)
except Exception as e:  # noqa
    print(f"Unable to bootstrap environment: {str(e)}", file=sys.stderr)
    sys.exit(1)
finally:
    Environment.teardown()
