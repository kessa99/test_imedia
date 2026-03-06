"""
useCase pour l'enregistrement d'un utilisateur
"""
from src.application.useCase.check_empty import check_empty
from src.application.service.checkPassword import check_password
from src.application.entities.user import UserEntity
from datetime import datetime
from src.utils.formatResponse import formatResponse


class RegisterUseCase:
    """
    useCase pour l'enregistrement d'un utilisateur
    """
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.check_empty = check_empty()
        self.check_mail = check_mail()
        self.check_password = check_password()

    def execute(self, register_dto):
        """
        exécution de l'useCase
        """
        # verifier si le nom, le mail et le password ne sont pas vide
        self.check_empty(register_dto.name, register_dto.email, register_dto.password)

        # verifier le fomat du mail
        self.check_mail(register_dto.email)

        # verifier si le mail existe
        mail_exist = self.user_repository.find_by_mail(register_dto.email)
        if mail_exist is not None:
            raise ValueError("L'email existe déjà")

        # verifier si le nom existe
        name_exist = self.user_repository.find_by_name(register_dto.name)
        if name_exist is not None:
            raise ValueError("Le nom existe déjà")

        # hasher le mot de passe
        hashed_password = self.check_password.hash(register_dto.password)

        # creer l'entite
        now = datetime.utcnow()
        user = UserEntity(
            id=uuid.uuid4(),
            name=register_dto.name,
            email=register_dto.email,
            password=hashed_password,
            created_at=now,
            updated_at=now
        )
        #save
        user = self.user_repository.save(user)
        return formatResponse(
            data=user,
            status_code=201,
            content= {
                "message": "Utilisateur enregistré avec succès",
                "data": user
            }
        )