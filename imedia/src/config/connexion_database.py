"""
Connexion à la base de données et générateur de session
"""

from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.config.settings import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Générateur de session SQLAlchemy pour l'injection de dépendances FastAPI (Depends).
    Garantit la fermeture de la session après chaque requête.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
