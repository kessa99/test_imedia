"""
Service pour vérifier qu'un champ n'est pas vide
"""


def check_empty(name: str, email: str, password: str) -> None:
    """
    Lève une ValueError si l'un des champs est vide.
    Note: avec Pydantic (RegisterDTO), cette validation est déjà faite en amont.
    """
    if not name:
        raise ValueError("Le nom est obligatoire")
    if not email:
        raise ValueError("L'email est obligatoire")
    if not password:
        raise ValueError("Le mot de passe est obligatoire")
