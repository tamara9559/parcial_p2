from app.models.user import User

class UserService:

    @staticmethod
    def create_user(db, name: str, email: str):
        user = User(name=name, email=email)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_user(db, user_id: int):
        return db.query(User).filter(User.id == user_id).first()


