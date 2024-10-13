from typing import Any
from flask import Flask


app = Flask(__name__)


@app.route('/')
def home() -> Any:
    return "Hello from Flask!"
