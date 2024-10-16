from config.environment import Environment

from web_app.api import api
# from web_app.app import app

__all__ = ["api"]

Environment.bootstrap()
