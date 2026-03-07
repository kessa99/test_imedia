"""
conftest pour les tests d'intégration
"""
import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker

from src.infrastructure.model.base import Base
import src.infrastructure.model.user_model  # noqa

TEST_DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER', 'test')}:{os.getenv('DB_PASSWORD', 'test')}"
    f"@{os.getenv('DB_HOST', 'localhost')}:{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'test_db')}"
)


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(TEST_DATABASE_URL, poolclass=NullPool)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()

    yield session

    session.close()
    Base.metadata.drop_all(engine)
    engine.dispose()
