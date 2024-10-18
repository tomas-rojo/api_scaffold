# from unittest.mock import patch

# from flask import Flask

# from config.settings.flask_webserver import FlaskWebserver


# def test_on_run_flask_webserver_is_started() -> None:
#     webserver = FlaskWebserver(host="127.0.0.1", listen_port=8001)
#     dummy_app = Flask("dummy")
#     with patch.object(dummy_app, "run", return_value=None) as mocked_run:
#         webserver.run(dummy_app)
#     mocked_run.assert_called_with(host="127.0.0.1", port=8001, debug=False)


# def test_with_debug_enabled_in_config_on_run_flask_webserver_is_started_in_debug_mode() -> None:
#     settings = FlaskSettings(debug=True)
#     webserver = WebserverFactory(settings).create()
#     dummy_app = Flask("dummy")
#     with patch.object(dummy_app, "run", return_value=None) as mocked_run:
#         webserver.run(dummy_app)
#     mocked_run.assert_called_with(host="0.0.0.0", port=8080, debug=True)
