from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user_integration():
    res = client.post("/users/", json={"name": "Ana", "email": "ana@test.com"})
    assert res.status_code == 200
    body = res.json()
    assert body["name"] == "Ana"


def test_create_task_integration():
    # Crear usuario
    u = client.post("/users/", json={"name": "Bob", "email": "bob@test.com"}).json()
    user_id = u["id"]

    # Crear tarea
    res = client.post(f"/tasks/{user_id}", json={"title": "Ir al gym", "description": "lunes"})
    assert res.status_code == 200
    data = res.json()
    assert data["title"] == "Ir al gym"
    assert data["user_id"] == user_id

