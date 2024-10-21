from flask.testing import FlaskClient


def test_index_should_return_200(flask_client: FlaskClient) -> None:
    response = flask_client.get("/")
    assert response.status_code == 200
    assert response.text == 'Hello from Flask!'