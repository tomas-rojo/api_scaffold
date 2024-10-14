from typing import Any

from config.dependency import Dependency
from flask import Flask
from ports.abstract_repository import AbstractRepository

app = Flask(__name__)


@app.route("/")
def home() -> Any:
    repository = Dependency.get(AbstractRepository)
    return "Hello from Flask!"
