from dataclasses import asdict
from random import randrange
from flask import Blueprint, Response, jsonify

from models.user import User
from use_cases.add_user import AddUserUseCase
from use_cases.get_user import GetUserUseCase

bp = Blueprint("users", __name__)


def get_random_value() -> int:
    return randrange(1000)


def do_email() -> str:
    return f"{get_random_value()}@gmail.com"


@bp.get("/")
def user() -> Response:
    user = User(email=do_email())
    AddUserUseCase(user).execute()
    return Response(response=f"Added user with ID: {user.id.hex}", status=201)


@bp.get("/<string:id>")
def get_user(id: str) -> Response:
    user = GetUserUseCase(user_id=id).execute()
    user_as_dict = asdict(user)
    print(asdict(user))
    return jsonify(user_as_dict)


@bp.put("/<string:id>")
def updated_user() -> Response:
    return Response("user from Blueprint!", status=200)


@bp.delete("/<string:id>")
def delete_user() -> Response:
    return Response("user from Blueprint!", status=200)


from fastapi import APIRouter

router = APIRouter()


# @router.post("/")
# def user(email: str):
#     return "Added user with ID: "


# @router.get("/{id}")
# def get_user(id: str):
#     return "user from Blueprint!"


# @router.put("/{id}")
# def updated_user(id: str):
#     return "user from Blueprint!"


# @router.delete("/{id}")
# def delete_user(id: str):
#     return "user from Blueprint!"
