from __future__ import annotations

from flask import Flask
from web_app.bootstrap import app

from config.settings.webserver.abstract_web_server import AbstractWebServer


class FlaskWebserver(AbstractWebServer):
    """A webserver implementation that makes use of the Flask built-in webserver,
    to make use of its automatic code reloading and debugging features."""

    def run(self, application: Flask) -> None:
        application.run(
            host=self.host,
            port=self.port,
            debug=True,
        )


if __name__ == "__main__":
    FlaskWebserver().run(app)
