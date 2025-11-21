from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_full_flow_e2e():
    # 1. Crear usuario
    user = client.post("/users/", json={"name": "Mario", "email": "mario@test.com"}).json()
    user_id = user["id"]

    # 2. Crear tarea
    task = client.post(f"/tasks/{user_id}", json={"title": "Comprar pan", "description": "para el desayuno"}).json()
    task_id = task["id"]

    # 3. Marcar como completada
    updated = client.put(f"/tasks/{task_id}?completed=true").json()
    assert updated["is_completed"] is True

    # 4. Listar tareas del usuario
    list_res = client.get(f"/tasks/{user_id}")
    assert list_res.status_code == 200
    assert len(list_res.json()) >= 1

    # 5. Eliminar la tarea
    delete_res = client.delete(f"/tasks/{task_id}")
    assert delete_res.status_code == 200

