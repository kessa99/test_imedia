"""
Test d'intégration pour l'enregistrement d'un utilisateur
"""
import pytest
from src.application.dto.register import RegisterDTO
from src.application.useCase.register import RegisterUseCase
from src.infrastructure.repoImpl.userRepo import UserRepoImpl


def test_register_persiste_le_user_en_base(db_session):
    repo = UserRepoImpl(db_session)
    dto = RegisterDTO(name="Alice", email="alice@example.com", password="password123")

    result = RegisterUseCase(repo).execute(dto)

    # La réponse est correcte
    assert result.name == "Alice"
    assert result.email == "alice@example.com"

    # Le user est bien en base
    persisted = repo.find_by_mail("alice@example.com")
    assert persisted is not None


def test_register_stocke_le_password_hashe_pas_en_clair(db_session):
    repo = UserRepoImpl(db_session)
    dto = RegisterDTO(name="Alice", email="alice@example.com", password="password123")

    RegisterUseCase(repo).execute(dto)

    persisted = repo.find_by_mail("alice@example.com")
    assert persisted.password != "password123"
    assert ":" in persisted.password  # format salt:hash


def test_register_email_duplique_leve_erreur_et_ne_sauvegarde_pas(db_session):
    repo = UserRepoImpl(db_session)
    dto1 = RegisterDTO(name="Alice", email="alice@example.com", password="password123")
    dto2 = RegisterDTO(name="Bob",   email="alice@example.com", password="password456")
    RegisterUseCase(repo).execute(dto1)

    with pytest.raises(ValueError, match="email est déjà utilisé"):
        RegisterUseCase(repo).execute(dto2)

    assert len(repo.find_all()) == 1  # toujours un seul user


def test_register_nom_duplique_leve_erreur(db_session):
    repo = UserRepoImpl(db_session)
    dto1 = RegisterDTO(name="Alice", email="alice@example.com", password="password123")
    dto2 = RegisterDTO(name="Alice", email="autre@example.com", password="password456")
    RegisterUseCase(repo).execute(dto1)

    with pytest.raises(ValueError, match="nom est déjà utilisé"):
        RegisterUseCase(repo).execute(dto2)
