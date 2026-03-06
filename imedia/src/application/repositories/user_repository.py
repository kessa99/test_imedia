"""
Interface abstraite du repository utilisateur.
Définit le contrat que toute implémentation doit respecter.
"""

from abc import ABC, abstractmethod
from uuid import UUID

from src.application.entities.user import UserEntity


class IUserRepository(ABC):
    """
    Port (au sens Clean Architecture) vers la persistance des utilisateurs.
    La couche Application ne connaît que cette interface, jamais l'implémentation concrète.
    """

    @abstractmethod
    def save(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def find_by_id(self, user_id: UUID) -> UserEntity | None:
        pass

    @abstractmethod
    def find_all(self) -> list[UserEntity]:
        pass

    @abstractmethod
    def find_by_mail(self, email: str) -> UserEntity | None:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> UserEntity | None:
        pass

    @abstractmethod
    def update(self, user: UserEntity) -> UserEntity:
        pass

    @abstractmethod
    def delete(self, user_id: UUID) -> None:
        pass
