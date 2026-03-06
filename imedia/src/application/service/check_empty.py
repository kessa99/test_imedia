"""
service pour s'assurer que les champs ne sont pas vide
"""

class check_empty:
    """
    service pour s'assurer que les champs ne sont pas vide
    """

    def check_empty(self, name, email, password):
        """
        service pour s'assurer que le nom ne soit pas vide
        """
        if not name:
            raise ValueError("Le nom est obligatoire")

        if not email:
            raise ValueError("L'email est obligatoire")

        if not password:
            raise ValueError("Le mot de passe est obligatoire")