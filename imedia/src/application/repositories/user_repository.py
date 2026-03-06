"""
Interface abstraite du repository pour les utilisateurs
il defini le contrat que toute implementation doit respecter
"""

from abc import ABC, abstractmethod
from uuid import UUID

from src.application.entities.user import UserEntity

class UserRepositoryImpl(ABC):
    """
    Interface abstraite du repository pour les utilisateurs
    il defini le contrat que toute implementation doit respecter
    """

    @abstractmethod
    def save(self, user: UserEntity) -> UserEntity:
        """
        sauvegarde d'un utilisateur
        """
        pass

    @abstractmethod
    def find_by_id(self, user_id: UUID) -> UserEntity:
        """
        recherche d'un utilisateur par son id
        """
        pass

    @abstractmethod
    def find_all(self) -> list[UserEntity]:
        """
        recherche de tous les utilisateurs
        """
        pass

    @abstractmethod
    def update(self, user: UserEntity) -> UserEntity:
        """
        mise à jour d'un utilisateur
        """
        pass

    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        """
        suppression d'un utilisateur
        """
        pass