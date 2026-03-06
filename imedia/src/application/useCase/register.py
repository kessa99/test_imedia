"""
Use case pour l'enregistrement d'un utilisateur
"""

import uuid
from datetime import datetime

from src.application.repositories.user_repository import IUserRepository
from src.application.dto.register import RegisterDTO
from src.application.dto.user_response import UserResponseDTO
from src.application.entities.user import UserEntity
from src.application.service.check_empty import check_empty
from src.application.service.check_format_mail import check_format_mail
from src.application.service.password_service import PasswordService


class RegisterUseCase:
    """
    Orchestre l'enregistrement d'un nouvel utilisateur.
    Ne dépend que d'interfaces (IUserRepository), jamais des implémentations concrètes.
    """

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
        self.password_service = PasswordService()

    def execute(self, register_dto: RegisterDTO) -> UserResponseDTO:
        check_empty(register_dto.name, register_dto.email, register_dto.password)
        check_format_mail(register_dto.email)

        if self.user_repository.find_by_mail(register_dto.email) is not None:
            raise ValueError("Cet email est déjà utilisé")

        if self.user_repository.find_by_name(register_dto.name) is not None:
            raise ValueError("Ce nom est déjà utilisé")

        hashed_password = self.password_service.hash(register_dto.password)

        now = datetime.utcnow()
        user = UserEntity(
            id=uuid.uuid4(),
            name=register_dto.name,
            email=register_dto.email,
            password=hashed_password,
            created_at=now,
            updated_at=now,
        )

        saved_user = self.user_repository.save(user)

        return UserResponseDTO(
            id=saved_user.id,
            name=saved_user.name,
            email=saved_user.email,
            created_at=saved_user.created_at,
            updated_at=saved_user.updated_at,
        )
