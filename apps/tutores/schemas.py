from drf_spectacular.utils import extend_schema

from apps.schemas_utils import (
    GENERIC_VALIDATION_ERROR_RESPONSE,
    associate_with_user,
    create_user,
)
from . import serializers


class TutorSchema:
    list = extend_schema(
        summary="Listagem de tutores",
        description="Requer permissão de veterinário.",
        responses=serializers.TutorSerializer(many=True),
    )

    create = extend_schema(
        summary="Cadastrar novo tutor",
        description="Apenas o veterinário pode cadastar um novo tutor. Envia todos os dados do user caso queira criar um, ou apenas o user_id caso já exista.",
        request=serializers.TutorCreateSerializer,
        responses={
            201: serializers.TutorSerializer,
            400: GENERIC_VALIDATION_ERROR_RESPONSE,
        },
        examples=[create_user("tutor"), associate_with_user("tutor")],
    )

    retrieve = extend_schema(
        summary="Obter detalhes do tutor",
        description="Requer permissão de veterinário, ou ser o próprio tutor.",
        responses=serializers.TutorSerializer,
    )

    update = extend_schema(
        summary="Atualizar tutor (completo)",
        description="Requer permissão de veterinário.",
        responses={
            200: serializers.TutorSerializer,
            400: GENERIC_VALIDATION_ERROR_RESPONSE,
        },
    )

    partial_update = extend_schema(
        summary="Atualizar tutor (parcial)",
        description="Requer permissão de veterinário.",
        responses={
            200: serializers.TutorSerializer,
            400: GENERIC_VALIDATION_ERROR_RESPONSE,
        },
    )

    destroy = extend_schema(
        summary="Deletar tutor", description="Requer permissão de veterinário."
    )
