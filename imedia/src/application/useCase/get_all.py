"""
Use case pour récupérer tous les utilisateurs
"""

from src.application.repositories.user_repository import IUserRepository
from src.application.dto.user_response import UserResponseDTO


class GetAllUseCase:
    """
    Récupère la liste de tous les utilisateurs.
    Ne dépend que de l'interface IUserRepository.
    """

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self) -> list[UserResponseDTO]:
        users = self.user_repository.find_all()
        return [
            UserResponseDTO(
                id=user.id,
                name=user.name,
                email=user.email,
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users
        ]
