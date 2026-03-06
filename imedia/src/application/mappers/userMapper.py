"""
Mapper User: Converti un UserModel SQL  en une entite du domais
"""

from src.application.entities.user import UserEntity
from src.infrastructure.model.userModel import User

def userModelToUserEntity(user: User) -> UserEntity:
    """
    Mapper User: Converti un UserModel SQL  en une entite du domais
    """
    return UserEntity(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password,
        created_at=user.created_at,
        updated_at=user.updated_at
    )

def userEntityToUserModel(user: UserEntity) -> User:
    """
    Mapper User: Converti une entite du domais en un UserModel SQL
    """
    return User(
        id=user.id,
        name=user.name,
        email=user.email,
        password=user.password,
        created_at=user.created_at,
        updated_at=user.updated_at
    )