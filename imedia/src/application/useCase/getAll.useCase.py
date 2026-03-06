"""
Use case pour récupérer tous les utilisateurs
"""

from src.application.entities.user import UserEntity
from src.utils.formatResponse import formatResponse

class GetAllUseCase:
    """
    Use case pour récupérer tous les utilisateurs
    """
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self):
        """
        Exécution de l'use case
        """
        users = self.user_repository.find_all()
        return formatResponse(
            data=users,
            status_code=200,
            content= {
                "message": "Utilisateurs récupérés avec succès",
                "data": users
            }
        )