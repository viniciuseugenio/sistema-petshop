from drf_spectacular.utils import extend_schema, OpenApiParameter

from apps.pets import serializers


class PetSchema:
    list = (
        extend_schema(
            summary="Listagem de pets",
            description="Veterinários veem todos. Tutores veem apenas seus pets.",
            parameters=[
                OpenApiParameter(
                    "tutor",
                    int,
                    OpenApiParameter.QUERY,
                    description="Para visualizar os pets de um tutor especifico",
                )
            ],
            responses={200: serializers.PetListSerializer(many=True)},
        ),
    )
    create = (
        extend_schema(
            summary="Cadastrar novo pet",
            description="Requer permissão de veterinário.",
            request=serializers.PetCreateSerializer,
            responses={201: serializers.PetDetailsSerializer},
        ),
    )
    retrieve = (
        extend_schema(
            summary="Obter detalhes de um pet",
            description="Retorna informações detalhadas de um pet específico, incluindo dados completos do tutor.",
        ),
    )
    update = (
        extend_schema(
            summary="Atualizar pet (completo)",
            description="Requer permissão de veterinário.",
        ),
    )
    partial_update = (
        extend_schema(
            summary="Atualizar pet (parcial)",
            description="Requer permissão de veterinário.",
        ),
    )
    destroy = (
        extend_schema(
            summary="Deletar pet",
            description="Requer permissão de administrador.",
        ),
    )
