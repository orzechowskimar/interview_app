from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_users_with_pagination():
    response = client.get("/users/?skip=0&limit=2")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) <= 2

def test_create_user_with_invalid_payload():
    response = client.post("/users/", json={
        "username": "baduser"
        # missing email
    })
    assert response.status_code == 422