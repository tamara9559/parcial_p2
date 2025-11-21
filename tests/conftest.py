import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker

os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from app.database import Base, create_engine_from_env, get_db
from app.main import app


@pytest.fixture(scope="function", autouse=True)
def setup_test_db():

    engine = create_engine_from_env()

    # Limpiar BD antes de cada test
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    TestingSessionLocal = sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(app)





