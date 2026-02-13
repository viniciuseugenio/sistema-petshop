from drf_spectacular.utils import OpenApiExample, OpenApiResponse


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


GENERIC_VALIDATION_ERROR_RESPONSE = OpenApiResponse(
    response={
        "type": "object",
        "additionalProperties": {
            "type": "array",
            "items": {"type": "string"},
        },
        "example": {
            "field_name": ["Erro 1", "Erro 2"],
            "another_field": ["Outro erro"],
        },
    },
    description="Erro de validação. Retorna um objeto onde cada chave é o nome do campo e o valor é uma lista de mensagens de erro.",
)
