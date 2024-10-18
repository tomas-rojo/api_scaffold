# from unittest.mock import patch

# from flask import Flask

# from config.settings.gunicorn_webserver import GunicornWebServer


# def test_standalone_gunicorn_application_passes_on_provided_flask_application() -> None:
#     dummy_app = Flask("dummy")
#     standalone_application = GunicornWebServer().FlaskApplication(dummy_app, {})
#     assert standalone_application.load() == dummy_app


# def test_on_run_gunicorn_webserver_is_started() -> None:
#     webserver = GunicornWebServer()
#     dummy_app = Flask("dummy")
#     with patch.object(GunicornWebServer, "run", return_value=None) as mocked_run:
#         webserver.run(dummy_app)
#     mocked_run.assert_called()


# def test_invalid_configuration_key_logs_error(assert_logs: AssertLogsType) -> None:
#     dummy_app = Flask("dummy")
#     with assert_logs(["Unsupported Gunicorn configuration key used: run_speed"]):
#         StandaloneGunicornApplication(application=dummy_app, options={"run_speed": "flashy"})
