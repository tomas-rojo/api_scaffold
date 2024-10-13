from config.settings.abstract_web_server import AbstractWebServer
import uvicorn

from typing import Any

from web_app.api import api


class FastAPIWebServer(AbstractWebServer):

    def run(self, application: Any | str) -> None:
        uvicorn.run(application,
                    port=self.port,
                    host=self.host,
                    workers=1 if self.debug else self.workers,
                    reload=self.debug)


if __name__ == "__main__":
    FastAPIWebServer().run("web_app.api:api")
