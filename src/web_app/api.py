from fastapi import FastAPI

api = FastAPI(title="Test")


@api.get("/")
async def main() -> dict[str, str]:
    return {"msg": "Hello World"}
