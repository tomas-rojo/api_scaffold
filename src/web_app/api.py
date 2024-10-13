from fastapi import FastAPI, Response
from use_cases.get_index import IndexUseCase

api = FastAPI(title="Test")


# @api.get("/")
# def main() -> dict[str, str]:
#     return {"result": IndexUseCase("1").execute()}

@api.get('/')
async def home() -> str:
    return "Hello from FastAPI!"
