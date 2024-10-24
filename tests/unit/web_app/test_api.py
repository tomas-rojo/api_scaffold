from starlette.testclient import TestClient

from services.command.add import add_element

def test_index_should_return_200(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == 'Hello from FastAPI!'