from sqlalchemy.orm import Session
from app.models.task import Task

class TaskService:

    @staticmethod
    def create_task(db: Session, title: str, description: str, user_id: int):
        new_task = Task(title=title, description=description, user_id=user_id)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task

    @staticmethod
    def list_tasks_by_user(db: Session, user_id: int):
        return db.query(Task).filter(Task.user_id == user_id).all()

    @staticmethod
    def update_task_status(db: Session, task_id: int, is_completed: bool):
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        task.is_completed = is_completed
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete_task(db: Session, task_id: int):
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False
        db.delete(task)
        db.commit()
        return True


