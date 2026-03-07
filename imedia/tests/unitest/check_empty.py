"""
Test unitaire pour la vérification des champs
"""

from src.application.useCase.check_empty import check_empty


def test_valid_fields_no_exception():
    """
    Test valide : tous les champs sont non vides
    """
    check_empty("toto", "toto@toto.com", "toto")


def test_invalid_name_exception():
    """
    Test invalide : le nom est vide
    """
    with pytest.raises(ValueError):
        check_empty("", "toto@toto.com", "toto")


def test_invalid_email_exception():
    """
    Test invalide : l'email est vide
    """
    with pytest.raises(ValueError):
        check_empty("toto", "", "toto")


def test_invalid_password_exception():
    """
    Test invalide : le mot de passe est vide
    """
    with pytest.raises(ValueError):
        check_empty("toto", "toto@toto.com", "")
