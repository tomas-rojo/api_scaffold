from typing import Any

from flask import Flask
from gunicorn.app.base import BaseApplication
from web_app.bootstrap import app

from config.settings.webserver.abstract_web_server import AbstractWebServer


class GunicornWebServer(AbstractWebServer):
    """A webserver implementation based on Gunicorn, to be used for production purposes."""

    # Ignore type, because gunicorn does not have type hints currently.
    class FlaskApplication(BaseApplication):  # type: ignore
        def __init__(self, app: Flask, options: dict[str, Any]) -> None:
            self.app = app
            self.options = options
            super().__init__()

        def load_config(self) -> None:
            config = {key: value for key, value in self.options.items()}
            for key, value in config.items():
                self.cfg.set(key, value)

        def load(self) -> Flask:
            return self.app

    def run(self, application: Flask) -> None:
        options = {
            "bind": f"{self.host}:{self.port}",
            "workers": self.workers,
        }
        self.FlaskApplication(application, options).run()


if __name__ == "__main__":  # noqa
    GunicornWebServer().run(app)
