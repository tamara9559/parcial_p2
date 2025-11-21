from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.task_schema import TaskCreate, TaskOut, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return TaskService.create_task(
        db,
        task.title,
        task.description,
        task.user_id
    )


@router.get("/user/{user_id}", response_model=list[TaskOut])
def list_tasks(user_id: int, db: Session = Depends(get_db)):
    return TaskService.list_tasks_by_user(db, user_id)

@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, update: TaskUpdate, db: Session = Depends(get_db)):
    return TaskService.update_task_status(
        db,
        task_id,
        update.is_completed
    )


@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    TaskService.delete_task(db, task_id)
    return {"message": "Task deleted"}
