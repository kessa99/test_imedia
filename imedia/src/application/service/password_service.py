"""
Service pour le hashage et la vérification des mots de passe
"""

import hashlib
import secrets


class PasswordService:
    """
    Service de hachage de mots de passe utilisant PBKDF2-SHA256 (builtin Python).
    """

    def hash(self, password: str) -> str:
        """Retourne un hash sécurisé du mot de passe"""
        salt = secrets.token_hex(16)
        key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100_000)
        return f"{salt}:{key.hex()}"

    def verify(self, plain: str, hashed: str) -> bool:
        """Vérifie qu'un mot de passe en clair correspond au hash stocké"""
        try:
            salt, key = hashed.split(":")
            new_key = hashlib.pbkdf2_hmac("sha256", plain.encode(), salt.encode(), 100_000)
            return new_key.hex() == key
        except Exception:
            return False
