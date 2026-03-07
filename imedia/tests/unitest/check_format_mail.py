"""
test pour la validation du  mail
"""

from src.application.useCase.check_format_mail import check_format_mail

def test_valid_mail_no_exception():
    """
    Test valide : le mail est valide
    """
    check_format_mail("toto@toto.com")

def test_invalid_email():
    """
    tester le format d'un email invalide
    """
    with pytest.raises(ValueError):
        check_format_mail("toto")

    with pytest.raises(ValueError):
        check_format_mail("toto@toto")

    with pytest.raises(ValueError):
        check_format_mail("toto@toto.com.fr")

def test_email_no_domain_raise():
    """
    tester le format d'un email sans domaine
    """
    with pytest.raises(ValueError, match="Fomat d'eamil invalide"):
        check_format_mail("toto@")

def test_email_too_long_raise():
    """
    tester le format d'un email trop long
    """
    with pytest.raises(ValueError, match="Fomat d'eamil invalide"):
        long_email = "a" * 256 + "@toto.com"
        with pytest.raises(ValueError, match="255 caractères"):
            check_format_mail(long_email)