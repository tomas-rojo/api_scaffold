from starlette.testclient import TestClient

def test_index_should_return_200(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}