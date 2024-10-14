import uuid
from random import randrange

from fastapi import FastAPI
from pydantic import BaseModel, Field
from use_cases.get_index import IndexUseCase

api = FastAPI(title="Test")


# @api.get("/")
# def main() -> dict[str, str]:
#     return {"result": IndexUseCase("1").execute()}
def get_random_value() -> int:
    return randrange(1000)


class Number(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    number: int = Field(default_factory=get_random_value)
    who: str


@api.get("/")
async def home() -> str:
    number = Number(who="sqlalchemy")
    # try:
    #     await _add_number(number)
    # except Exception as e:
    #     return {"error": str(e)}
    return "Hello from FastAPI!"
