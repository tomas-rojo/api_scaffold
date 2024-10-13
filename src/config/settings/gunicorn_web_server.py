from config.settings.abstract_web_server import AbstractWebServer


from flask import Flask
from gunicorn.app.base import BaseApplication

from web_app.app import app


class GunicornWebServer(AbstractWebServer):
    def run(self, application: Flask) -> None:
        options = {
            'bind': f'{self.host}:{self.port}',
            'workers': 4,
        }
        BaseApplication(application, options).run()

if __name__ == "__main__":
    GunicornWebServer().run(app)
