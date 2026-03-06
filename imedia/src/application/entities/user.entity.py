"""
Entité représentant un utilisateur
"""

import uuid
from datetime import datetime
from datetime import datetime, date
from pydantic import BaseModel

class UserEntity(BaseModel):
    """
    Entité représentant un utilisateur
    """
    id: UUID
    name: str
    email: str
    password: str
    created_at: datetime
    updated_at: datetime