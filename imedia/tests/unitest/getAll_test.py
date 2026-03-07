"""
Test unitaire pour la récupération de tous les utilisateurs use case
"""

from datetime import datetime
from unittest.mock import MagicMock
from uuid import uuid4

from src.application.dto.user_response import UserResponseDTO
from src.application.useCase.get_all import GetAllUseCase
from src.application.repositories.user_repository import IUserRepository
from src.application.entities.user import UserEntity

now = datetime.utcnow()

class MockUserRepository(IUserRepository):
    """
    Mock pour le repository utilisateur
    """
    def find_all(self) -> list[UserEntity]:
        return []


def test_get_all_returns_empty_list_when_no_users():
    repo = MagicMock(spec=IUserRepository)
    repo.find_all.return_value = []
    result = GetAllUseCase(repo).execute()
    assert result == []

def test_get_all_returns_mapped_users():
    repo = MagicMock(spec=IUserRepository)
    repo.find_all.return_value = [
        UserEntity(id=uuid4(), name="Alice", email="a@a.com",
                   password="hash", created_at=now, updated_at=now),
        UserEntity(id=uuid4(), name="Bob", email="b@b.com",
                   password="hash", created_at=now, updated_at=now),
    ]
    result = GetAllUseCase(repo).execute()
    assert len(result) == 2
    assert result[0].name == "Alice"
    assert result[1].email == "b@b.com"
