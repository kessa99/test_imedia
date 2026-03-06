"""
Entité représentant un utilisateur dans le domaine
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class UserEntity:
    """
    Entité de domaine - aucune dépendance vers l'infrastructure ou le framework
    """
    id: UUID
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime
