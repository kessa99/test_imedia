"""
Service pour valider le format d'un email
"""

import re


def check_format_mail(email: str) -> None:
    """
    Lève une ValueError si le format de l'email est invalide.
    Note: avec Pydantic (EmailStr dans RegisterDTO), cette validation est déjà faite en amont.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValueError("Format d'email invalide")

    if len(email) > 255:
        raise ValueError("L'email ne peut pas dépasser 255 caractères")
