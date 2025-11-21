from app.models.task import Task

class TaskService:

    @staticmethod
    def create_task(db, title: str, description: str, user_id: int):
        task = Task(title=title, description=description, user_id=user_id)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def set_completed(db, task_id: int, completed: bool):
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        
        task.is_completed = completed
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete_task(db, task_id: int):
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None

        db.delete(task)
        db.commit()
        return True

    @staticmethod
    def list_by_user(db, user_id: int):
        return db.query(Task).filter(Task.user_id == user_id).all()



