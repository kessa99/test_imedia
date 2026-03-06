"""
DTOs pour l'enregistrement d'un utilisateur
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class RegisterDTO(BaseModel):
    """DTO pour l'inscription (création d'un owner)"""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)