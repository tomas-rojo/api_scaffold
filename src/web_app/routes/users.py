from flask import Blueprint

bp = Blueprint("users", __name__)


@bp.post("/users")
def user():
    return "Added user with ID: "


@bp.get("/users/<str:id>")
def get_user():
    return "user from Blueprint!"


@bp.put("/users/<str:id>")
def updated_user():
    return "user from Blueprint!"


@bp.delete("/users/<str:id>")
def delete_user():
    return "user from Blueprint!"


from fastapi import APIRouter

router = APIRouter()


# @router.post("/users")
# def user(email: str):
#     return "Added user with ID: "


@router.get("/users/{id}")
def get_user(id: str):
    return "user from Blueprint!"


# @router.put("/users/{id}")
# def updated_user(id: str):
#     return "user from Blueprint!"


# @router.delete("/users/{id}")
# def delete_user(id: str):
#     return "user from Blueprint!"
