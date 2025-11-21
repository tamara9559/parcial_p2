from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(String(500))
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
