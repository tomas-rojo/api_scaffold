from flask import Flask
from web_app.bootstrap import app

from config.settings.webserver.abstract_web_server import AbstractWebServer


class FlaskWebserver(AbstractWebServer):
    def run(self, application: Flask) -> None:
        application.run(
            host=self.host,
            port=self.port,
            debug=True,
        )


if __name__ == "__main__":
    FlaskWebserver().run(app)
