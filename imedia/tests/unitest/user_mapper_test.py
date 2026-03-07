"""
Test unitaire pour le mapper utilisateur
"""

from src.application.mappers.userMapper import userEntityToUserModel, userModelToUserEntity
from src.infrastructure.model.user_model import User
from src.application.entities.user import UserEntity

def test_user_model_to_user_entity():
    """
    Test valide : mapper userModelToUserEntity
    """
    user = User(
        id=uuid4(),
        name="toto",
        email="toto@toto.com",
        password="hash",
        created_at=now,
        updated_at=now
    )
    user_entity = userModelToUserEntity(user)
    assert user_entity.id == user.id
    assert user_entity.name == user.name
    assert user_entity.email == user.email
    assert user_entity.password == user.password
    assert user_entity.created_at == user.created_at
    assert user_entity.updated_at == user.updated_at

def test_user_entity_to_user_model():
    """
    Test valide : mapper userEntityToUserModel
    """
    user = UserEntity(
        id=uuid4(),
        name="toto",
        email="toto@toto.com",
        password="hash",
        created_at=now,
        updated_at=now
    )
    user_model = userEntityToUserModel(user)
    assert user_model.id == user.id
    assert user_model.name == user.name
    assert user_model.email == user.email
    assert user_model.password == user.password
    assert user_model.created_at == user.created_at
    assert user_model.updated_at == user.updated_at