from typing import Any

import uvicorn

from config.settings.webserver.abstract_web_server import AbstractWebServer


class FastAPIWebServer(AbstractWebServer):
    def run(self, application: Any | str) -> None:
        uvicorn.run(
            application, port=self.port, host=self.host, workers=1 if self.debug else self.workers, reload=self.debug
        )


if __name__ == "__main__":  # pragma: no cover
    FastAPIWebServer().run("web_app.bootstrap:api")
