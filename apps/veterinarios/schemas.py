from drf_spectacular.utils import OpenApiExample, extend_schema
from . import serializers
from apps.schemas_utils import (
    GENERIC_VALIDATION_ERROR_RESPONSE,
    create_user,
    associate_with_user,
)


class VeterinarioSchema:
    list = extend_schema(
        summary="Listagem de veterinários",
        description="Requer permissão de veterinário.",
        responses=serializers.VeterinarioSerializer(many=True),
    )

    create = extend_schema(
        summary="Cadastrar novo veterinário",
        description="Requer permissão de administrador. Envia todos os dados do user caso queira criar um, ou apenas o user_id caso já exista.",
        request=serializers.VeterinarioCreateSerializer,
        responses={
            201: serializers.VeterinarioSerializer,
            400: GENERIC_VALIDATION_ERROR_RESPONSE,
        },
        examples=[create_user("veterinário"), associate_with_user("veterinário")],
    )

    retrieve = extend_schema(
        summary="Obter detalhes do veterinário",
        description="Requer permissão de veterinário.",
        responses=serializers.VeterinarioSerializer,
    )

    update = extend_schema(
        summary="Atualizar veterinário (completo)",
        description="O usuário deve ser o próprio veterinário.",
        request=serializers.VeterinarioSerializer,
        responses={
            200: serializers.VeterinarioSerializer,
            400: GENERIC_VALIDATION_ERROR_RESPONSE,
        },
    )

    partial_update = extend_schema(
        summary="Atualizar veterinário (parcial)",
        description="O usuário deve ser o próprio veterinário.",
        request=serializers.VeterinarioSerializer,
        responses={
            200: serializers.VeterinarioSerializer,
            400: GENERIC_VALIDATION_ERROR_RESPONSE,
        },
    )

    destroy = extend_schema(
        summary="Deletar veterinário", description="Request permissão de administrador"
    )
