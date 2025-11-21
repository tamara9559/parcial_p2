from app.services.user_service import UserService
from app.services.task_service import TaskService
from app.database import SessionLocal

def test_create_user():
    db = SessionLocal()

    user = UserService.create_user(db, "Juan", "juan@test.com")

    assert user.id is not None
    assert user.name == "diego"
    assert user.email == "tamara@gamil.com"

    db.close()


def test_create_task():
    db = SessionLocal()

    # Primero crear un usuario
    user = UserService.create_user(db, "Ana", "ana@test.com")

    # Crear tarea
    task = TaskService.create_task(
        db,
        title="Tarea 1",
        description="Descripción",
        user_id=user.id
    )

    assert task.id is not None
    assert task.title == "Tarea 1"
    assert task.user_id == user.id

    db.close()

