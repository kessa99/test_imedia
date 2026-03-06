"""
Router principal de l'API V1
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.config.connexion_database import get_db
from src.application.dto.register import RegisterDTO
from src.application.dto.user_response import UserResponseDTO
from src.infrastructure.repoImpl.userRepo import UserRepoImpl
from src.interface.api.v1.auth_controller.register import RegisterController

router = APIRouter()


@router.post("/register", response_model=UserResponseDTO, status_code=201)
def register(register_dto: RegisterDTO, db: Session = Depends(get_db)):
    """Enregistrement d'un nouvel utilisateur"""
    repo = UserRepoImpl(db)
    controller = RegisterController(repo)
    try:
        return controller.register(register_dto)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users", response_model=list[UserResponseDTO])
def get_all(db: Session = Depends(get_db)):
    """Récupération de tous les utilisateurs"""
    repo = UserRepoImpl(db)
    controller = RegisterController(repo)
    return controller.get_all()
