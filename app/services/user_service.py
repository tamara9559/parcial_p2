from sqlalchemy.orm import Session
from app.models.user import User

class UserService:

    @staticmethod
    def create_user(db: Session, name: str, email: str):
        new_user = User(name=name, email=email)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_all_users(db: Session):
        return db.query(User).all()

    @staticmethod
    def delete_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        db.delete(user)
        db.commit()
        return True

