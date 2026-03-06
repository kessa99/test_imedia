"""
Initialisation de la base de données (création des tables)
"""

from src.config.connexion_database import engine
from src.infrastructure.model.base import Base
import src.infrastructure.model.user_model  # noqa: F401 — enregistre le modèle User auprès de la Base


def init_db() -> None:
    """
    Crée toutes les tables définies dans les modèles SQLAlchemy.
    À appeler au démarrage de l'application (startup event FastAPI).
    """
    Base.metadata.create_all(bind=engine)
