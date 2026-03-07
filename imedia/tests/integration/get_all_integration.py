"""
Test d'intégration pour la récupération de tous les utilisateurs
"""

from src.application.useCase.register import RegisterUseCase
from src.application.useCase.get_all import GetAllUseCase
from src.application.dto.register import RegisterDTO
from src.infrastructure.repoImpl.userRepo import UserRepoImpl


def test_get_all_retourne_liste_vide_si_aucun_user(db_session):
    repo = UserRepoImpl(db_session)

    result = GetAllUseCase(repo).execute()

    assert result == []


def test_get_all_retourne_tous_les_users_enregistres(db_session):
    repo = UserRepoImpl(db_session)
    RegisterUseCase(repo).execute(
        RegisterDTO(name="Alice", email="alice@example.com", password="password123")
    )
    RegisterUseCase(repo).execute(
        RegisterDTO(name="Bob", email="bob@example.com", password="password456")
    )

    result = GetAllUseCase(repo).execute()

    assert len(result) == 2
    emails = {u.email for u in result}
    assert emails == {"alice@example.com", "bob@example.com"}


def test_get_all_ne_retourne_pas_les_passwords(db_session):
    repo = UserRepoImpl(db_session)
    RegisterUseCase(repo).execute(
        RegisterDTO(name="Alice", email="alice@example.com", password="password123")
    )

    result = GetAllUseCase(repo).execute()

    # UserResponseDTO ne doit pas exposer le password
    assert not hasattr(result[0], "password")
