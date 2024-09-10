from fastapi import FastAPI
from use_cases.get_index import IndexUseCase

api = FastAPI(title="Test")


@api.get("/")
def main() -> dict[str, str]:
    return {"result": IndexUseCase("1").execute()}
