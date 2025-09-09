from fastapi.testclient import TestClient

from nixpack_template.server import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


if __name__ == "__main__":
    test_read_main()
