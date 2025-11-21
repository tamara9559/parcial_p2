from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.task_schema import TaskCreate, TaskResponse
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/{user_id}", response_model=TaskResponse)
def create_task(user_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return TaskService.create_task(db, task.title, task.description, user_id)

@router.put("/{task_id}", response_model=TaskResponse)
def set_completed(task_id: int, completed: bool, db: Session = Depends(get_db)):
    return TaskService.set_completed(db, task_id, completed)

@router.get("/{user_id}", response_model=list[TaskResponse])
def list_tasks(user_id: int, db: Session = Depends(get_db)):
    return TaskService.list_by_user(db, user_id)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    TaskService.delete_task(db, task_id)
    return {"message": "Deleted"}

