"""
Controller pour l'authentification (register, getAll)
"""

from src.application.dto.register import RegisterDTO
from src.application.dto.user_response import UserResponseDTO
from src.application.repositories.user_repository import IUserRepository
from src.application.useCase.register import RegisterUseCase
from src.application.useCase.get_all import GetAllUseCase


class RegisterController:
    """
    Controller mince : délègue toute la logique aux Use Cases.
    Reçoit un IUserRepository injecté par le router via FastAPI Depends.
    """

    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def register(self, register_dto: RegisterDTO) -> UserResponseDTO:
        use_case = RegisterUseCase(self.user_repository)
        return use_case.execute(register_dto)

    def get_all(self) -> list[UserResponseDTO]:
        use_case = GetAllUseCase(self.user_repository)
        return use_case.execute()
