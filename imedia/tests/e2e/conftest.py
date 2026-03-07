"""
conftest pour les tests e2e
"""

import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker

from src.main import create_app
from src.config.connexion_database import get_db
from src.infrastructure.model.base import Base
import src.infrastructure.model.user_model  # noqa

TEST_DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER', 'test')}:{os.getenv('DB_PASSWORD', 'test')}"
    f"@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'test_db')}"
)


@pytest.fixture(scope="function")
def client():
    engine = create_engine(TEST_DATABASE_URL, poolclass=NullPool)
    Base.metadata.create_all(engine)
    TestingSession = sessionmaker(bind=engine)

    def override_get_db():
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()

    app = create_app()
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    Base.metadata.drop_all(engine)
    engine.dispose()
