"""
tester le hasher et le vérificateur de mot de passe
"""

from src.application.service.checkPassword import PasswordService

def test_hash_returns_string_with_salt_and_key():
    """
    Test valide : le hasher retourne une chaine de caractères avec un salt et une clé
    """
    password_service = PasswordService()
    hashed = password_service.hash("toto")
    assert isinstance(hashed, str)
    assert len(hashed.split(":")) == 2


def test_verify_returns_true():
    """
    Test valide : le vérificateur retourne True
    """
    password_service = PasswordService()
    hashed = password_service.hash("toto")
    assert password_service.verify("toto", hashed)


def test_verify_returns_false():
    """
    Test invalide : le vérificateur retourne False
    """
    password_service = PasswordService()
    hashed = password_service.hash("toto")
    assert not password_service.verify("tata", hashed)

def test_hash_is_different_each_call():
    """
    Test valide : le hasher retourne une chaine de caractères avec un salt et une clé
    """
    password_service = PasswordService()
    hashed = password_service.hash("toto")
    hashed2 = password_service.hash("toto")
    assert hashed != hashed2
    assert hashed.split(":")[1] != hashed2.split(":")[1]