from ipaddress import IPv4Address
from unittest.mock import patch

import uvicorn

from config.settings.webserver.fastapi_webserver import FastAPIWebServer


def test_on_run_gunicorn_webserver_is_started() -> None:
    webserver = FastAPIWebServer(host="1.2.3.4", port=4343, debug=False, workers=2)
    dummy_app = "dummy:app"
    with patch.object(uvicorn, "run", return_value=None) as mocked_run:
        webserver.run(dummy_app)
    mocked_run.assert_called_with('dummy:app', workers=2, host="1.2.3.4", port=4343, reload=False)



def test_with_debug_enabled_webserver_automatically_reloads_on_code_changes() -> None:
    webserver = FastAPIWebServer(port=8080, debug=True, workers=1)
    dummy_app = "dummy:app"
    with patch.object(uvicorn, "run", return_value=None) as mocked_run:
        webserver.run(dummy_app)
    # The workers must are forced to 1 by debug mode, as required by uvicorn.
    mocked_run.assert_called_with("dummy:app", workers=1, host="0.0.0.0", port=8080, reload=True)
