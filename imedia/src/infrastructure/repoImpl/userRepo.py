"""
Implémentation concrète du repository utilisateur (SQLAlchemy + PostgreSQL)
"""

from uuid import UUID
from sqlalchemy.orm import Session

from src.application.entities.user import UserEntity
from src.application.repositories.user_repository import IUserRepository
from src.infrastructure.model.user_model import User
from src.infrastructure.mappers.user_mapper import user_entity_to_model, user_model_to_entity


class UserRepoImpl(IUserRepository):
    """
    Implémentation SQLAlchemy de IUserRepository.
    Appartient à la couche Infrastructure.
    """

    def __init__(self, session: Session):
        self.session = session

    def save(self, user: UserEntity) -> UserEntity:
        user_model = user_entity_to_model(user)
        self.session.add(user_model)
        self.session.commit()
        self.session.refresh(user_model)
        return user_model_to_entity(user_model)

    def find_by_id(self, user_id: UUID) -> UserEntity | None:
        user_model = self.session.query(User).filter(User.id == user_id).first()
        if user_model is None:
            return None
        return user_model_to_entity(user_model)

    def find_all(self) -> list[UserEntity]:
        users = self.session.query(User).all()
        return [user_model_to_entity(u) for u in users]

    def find_by_mail(self, email: str) -> UserEntity | None:
        user_model = self.session.query(User).filter(User.email == email).first()
        if user_model is None:
            return None
        return user_model_to_entity(user_model)

    def find_by_name(self, name: str) -> UserEntity | None:
        user_model = self.session.query(User).filter(User.name == name).first()
        if user_model is None:
            return None
        return user_model_to_entity(user_model)

    def update(self, user: UserEntity) -> UserEntity:
        user_model = self.session.query(User).filter(User.id == user.id).first()
        if user_model is None:
            raise ValueError("Utilisateur introuvable")
        user_model.name = user.name
        user_model.email = user.email
        user_model.password = user.password
        user_model.updated_at = user.updated_at
        self.session.commit()
        self.session.refresh(user_model)
        return user_model_to_entity(user_model)

    def delete(self, user_id: UUID) -> None:
        user_model = self.session.query(User).filter(User.id == user_id).first()
        if user_model is not None:
            self.session.delete(user_model)
            self.session.commit()
