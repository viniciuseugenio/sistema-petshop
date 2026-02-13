from drf_spectacular.utils import OpenApiExample


def create_user(userType):
    return OpenApiExample(
        "Criando novo usuário",
        description=f"Cria um novo usuário junto com o {userType}",
        value={
            "username": "maria",
            "first_name": "Maria",
            "last_name": "Santos",
            "email": "maria@gmail.com",
            "password": "senha123",
            "celular": "12345958901",
        },
        request_only=True,
    )


def associate_with_user(userType):
    return OpenApiExample(
        "Usando usuário existente",
        description=f"Associa um usuário já existe como {userType}",
        value={
            "user_id": 3,
            "celular": "12345958901",
        },
        request_only=True,
    )
