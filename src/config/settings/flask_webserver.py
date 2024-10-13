from config.settings.abstract_web_server import AbstractWebServer

from flask import Flask

from web_app.app import app


class FlaskWebserver(AbstractWebServer):

    def run(self, application: Flask) -> None:
        application.run(
            host=self.host,
            port=self.port,
            debug=self.debug,
        )

if __name__ == "__main__":
    FlaskWebserver().run(app)
