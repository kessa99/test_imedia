"""
DTO pour l'enregistrement d'un utilisateur
"""

from pydantic import BaseModel, EmailStr, Field


class RegisterDTO(BaseModel):
    """DTO d'entrée pour l'inscription d'un utilisateur"""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)
