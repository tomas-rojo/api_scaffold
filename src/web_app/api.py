import uuid
from random import randrange

from fastapi import FastAPI
from models.user import User
from services.command.add import add_element
from use_cases.get_index import IndexUseCase

from web_app.routes import users

api = FastAPI(title="Test")
api.include_router(users.router, prefix="/users")

# @api.get("/")
# def main() -> dict[str, str]:
#     return {"result": IndexUseCase("1").execute()}


def get_random_value() -> int:
    return randrange(1000)


def do_email() -> str:
    return f"{get_random_value()}@gmail.com"


@api.get("/")
async def home() -> str:
    user = User(email=do_email())
    add_element(user)
    return "Hello from FastAPI!"
