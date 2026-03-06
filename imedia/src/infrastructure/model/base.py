"""
Base SQLAlchemy partagée par tous les modèles
"""

from sqlalchemy.orm import declarative_base

Base = declarative_base()
