"""
Mapper User : convertit entre UserEntity (domaine) et User (SQLAlchemy).
Appartient à la couche Infrastructure car il connaît le modèle SQLAlchemy.
"""

from src.application.entities.user import UserEntity
from src.infrastructure.model.user_model import User


def user_model_to_entity(user: User) -> UserEntity:
    return UserEntity(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


def user_entity_to_model(user: UserEntity) -> User:
    return User(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )
