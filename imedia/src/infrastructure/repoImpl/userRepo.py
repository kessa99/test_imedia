"""
Implementation du repository user
"""

from sqlalchemy.orm import Session

from src.application.entities.user import UserEntity
from src.application.mappers.userMapper import userEntityToUserModel as map_entity_to_user_model
from src.application.mappers.userMapper import userModelToUserEntity as map_user_model_to_entity

class UserRepoImpl:
    """
    Implementation du repository user
    """
    def __init__(self, session: Session):
        self.session = session

    def save(self, user: UserEntity) -> UserEntity:
        """
        sauvegarde d'un utilisateur
        """
        user_model = map_entity_to_user_model(user)
        self.session.add(user_model)
        self.session.commit()
        return map_user_model_to_entity(user_model)
    
    def find_by_id(self, user_id: UUID) -> UserEntity:
        """
        recherche d'un utilisateur par son id
        """
        user_model = self.session.query(User).filter(User.id == user_id).first()
        return map_user_model_to_entity(user_model)

    def find_all(self) -> list[UserEntity]:
        """
        recherche de tous les utilisateurs
        """
        users = self.session.query(User).all()
        return [map_user_model_to_entity(user) for user in users]

    def find_by_mail(self, email: str) -> UserEntity:
        """
        recherche d'un utilisateur par son email
        """
        user_model = self.session.query(User).filter(User.email == email).first()
        if user_model is None:
            return None
        return map_user_model_to_entity(user_model)