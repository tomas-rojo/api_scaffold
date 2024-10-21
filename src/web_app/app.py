from typing import Any

from flask import Flask

from web_app.routes import users

app = Flask(__name__)
app.register_blueprint(users.bp, url_prefix="/users")


@app.route("/")
def home() -> Any:
    return "Hello from Flask!"
