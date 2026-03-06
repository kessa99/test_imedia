"""
connexion à la base de données et initialisation des modèles
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import settings
from config.connexion_database import Base

def init_db():
    """
    initialisation de la base de données
    """
    Base.metadata.create_all(bind=engine)
    return Base

Base = init_db()