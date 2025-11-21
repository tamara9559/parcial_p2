from app.services.user_service import UserService
from app.services.task_service import TaskService
from app.database import get_db

def test_create_user():

    for db in get_db():
        user = UserService.create_user(db, "Juan", "juan@test.com")

        assert user.id is not None
        assert user.name == "Juan"
        assert user.email == "juan@test.com"
        break

def test_create_task():

    for db in get_db():
        user = UserService.create_user(db, "Ana", "ana@test.com")

        task = TaskService.create_task(
            db,
            "Tarea 1",
            "Descripción",
            user.id
        )

        assert task.id is not None
        assert task.title == "Tarea 1"
        assert task.user_id == user.id
        break


