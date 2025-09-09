from fastapi.testclient import TestClient

from nixpack_template.server import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_items_without_param():
    item_id = 4
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": None}


def test_get_items_with_param():
    item_id = 4
    q = "foo"
    response = client.get(f"/items/{item_id}", params={"q": q})
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": q}


if __name__ == "__main__":
    test_get_items_with_param()
