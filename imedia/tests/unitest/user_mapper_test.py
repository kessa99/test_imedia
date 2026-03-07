"""
Test unitaire pour le mapper utilisateur
"""
from uuid import uuid4
from datetime import datetime

from src.infrastructure.mappers.user_mapper import user_entity_to_model, user_model_to_entity
from src.infrastructure.model.user_model import User
from src.application.entities.user import UserEntity

now = datetime.utcnow()

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
    user_entity = user_model_to_entity(user)
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
    user_model = user_entity_to_model(user)
    assert user_model.id == user.id
    assert user_model.name == user.name
    assert user_model.email == user.email
    assert user_model.password == user.password
    assert user_model.created_at == user.created_at
    assert user_model.updated_at == user.updated_at