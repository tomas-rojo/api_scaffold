import os
import signal
import subprocess
import sys
from multiprocessing import Process
from pathlib import Path
from pprint import pprint
from types import FrameType

import click
from adapters.sql_repository import SQLRepository
from config.dependency import Dependency
from config.environment import Environment
from ports.abstract_repository import AbstractRepository
from shared.alembic import AlembicUpgrade

PROG_NAME = "testctl"


@click.group
def cli() -> None:
    """Test Provisioning System CLI"""
    pass


def web_process() -> subprocess.Popen[bytes]:
    env = dict(os.environ)
    command = [sys.executable, "src/config/settings/fastapi_webserver.py"]
    return subprocess.Popen(args=command, env=env, cwd=os.getcwd())


def signal_handler(signal: int, frame: FrameType | None, process: subprocess.Popen[bytes]) -> None:
    """Handles signals and ensures cleanup of the web server process."""
    terminate_process(process)


def terminate_process(process: subprocess.Popen[bytes]) -> None:
    """Send termination signal to process and ensure it's cleaned up."""
    if process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=3)
        except subprocess.TimeoutExpired:
            process.kill()


def run_web_server() -> None:
    """Start the Web Server"""
    web_server_process = web_process()

    # Register signal handlers for clean shutdown
    signal.signal(signal.SIGINT, lambda signal, frame: signal_handler(signal, frame, web_server_process))
    signal.signal(signal.SIGTERM, lambda signal, frame: signal_handler(signal, frame, web_server_process))

    try:
        web_server_process.wait()  # Block and wait for the subprocess to finish
    except Exception as e:  # noqa
        print(f"Exception occurred: {e}")
    finally:
        terminate_process(web_server_process)


@cli.command()
def run() -> None:
    """Start the webserver process"""
    repository = Dependency.get(AbstractRepository)
    if isinstance(repository, SQLRepository):
        script_location = Path(__file__).parent.parent / "migrations"
        AlembicUpgrade(script_location).execute()
    try:
        web_server_process = Process(target=run_web_server)
        web_server_process.start()
        web_server_process.join()
    except KeyboardInterrupt:
        pass
    finally:
        if web_server_process.is_alive():
            web_server_process.terminate()
            web_server_process.join()


@cli.command()
def config() -> dict[str, str]:
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
