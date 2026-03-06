"""
DTO de réponse pour un utilisateur (sans le mot de passe)
"""

from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class UserResponseDTO(BaseModel):
    """DTO retourné au client - ne contient jamais le mot de passe"""
    id: UUID
    name: str
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
