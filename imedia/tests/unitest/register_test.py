"""
Test unitaire pour l'enregistrement d'un utilisateur use case
"""

from src.application.dto.register import RegisterDTO
from src.application.useCase.register import RegisterUseCase
from src.application.repositories.user_repository import IUserRepository
from src.application.entities.user import UserEntity

class MockUserRepository(IUserRepository):
    """
    Mock pour le repository utilisateur
    """
    def save(self, user: UserEntity) -> UserEntity:
        return user
    def find_by_id(self, user_id: UUID) -> UserEntity | None:
        return None
    def find_all(self) -> list[UserEntity]:
        return []
    def find_by_mail(self, email: str) -> UserEntity | None:
        return None
    def find_by_name(self, name: str) -> UserEntity | None:
        return None
    def update(self, user: UserEntity) -> UserEntity:
        return user
    def delete(self, user_id: UUID) -> None:
        pass
    return MockUserRepository()

def test_register_valid_no_exception():
    """
    Test valide : enregistrement d'un utilisateur valide
    """
    register_dto = RegisterDTO(
        name="toto",
        email="toto@toto.com",
        password="toto"
    )
    use_case = RegisterUseCase(MockUserRepository())
    user = use_case.execute(register_dto)
    assert user.name == "toto"
    assert user.email == "toto@toto.com"
    assert user.password == "toto"

def test_register_invalid_name_exception():
    """
    Test invalide : enregistrement d'un utilisateur invalide (nom vide)
    """
    register_dto = RegisterDTO(
        name="",
        email="toto@toto.com",
        password="toto"
    )
    use_case = RegisterUseCase(MockUserRepository())
    with pytest.raises(ValueError):
        use_case.execute(register_dto)

def test_register_invalid_email_exception():
    """
    Test invalide : enregistrement d'un utilisateur invalide (email vide)
    """
    register_dto = RegisterDTO(
        name="toto",
        email="",
        password="toto"
    )
    use_case = RegisterUseCase(MockUserRepository())
    with pytest.raises(ValueError):
        use_case.execute(register_dto)

def test_register_invalid_password_exception():
    """
    Test invalide : enregistrement d'un utilisateur invalide (mot de passe vide)
    """
    register_dto = RegisterDTO(
        name="toto",
        email="toto@toto.com",
        password=""
    )
    use_case = RegisterUseCase(MockUserRepository())
    with pytest.raises(ValueError):
        use_case.execute(register_dto)