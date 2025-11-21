import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

def create_engine_from_env():
    url = os.getenv("DATABASE_URL", "mysql+pymysql://root:@localhost/parcial")
    engine = create_engine(
        url,
        connect_args={"check_same_thread": False} if url.startswith("sqlite") else {}
    )
    return engine

engine = create_engine_from_env()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




