from flask import Blueprint

bp = Blueprint("users", __name__)


@bp.post("/")
def user():
    return "Added user with ID: "


@bp.get("/<string:id>")
def get_user():
    return "user from Blueprint!"


@bp.put("/<string:id>")
def updated_user():
    return "user from Blueprint!"


@bp.delete("/<string:id>")
def delete_user():
    return "user from Blueprint!"


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
