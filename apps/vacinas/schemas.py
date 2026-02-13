from drf_spectacular.utils import extend_schema, OpenApiParameter
from . import serializers


class VacinaSchema:
    list = extend_schema(
        summary="Listagem de vacinas",
        description="Requer permissão de veterinário. Lista todas as unidades de vacinas disponíveis no sistema.",
        responses={200: serializers.VacinaSerializer(many=True)},
    )

    create = extend_schema(
        summary="Cadastrar nova vacina",
        description="Requer permissão de veterinário. Cria uma nova unidade de vacina.",
        request=serializers.VacinaSerializer,
        responses={201: serializers.VacinaSerializer},
    )

    retrieve = extend_schema(
        summary="Obter detalhes da vacina",
        description="Requer permissão de veterinário.",
        responses={200: serializers.VacinaSerializer},
    )

    update = extend_schema(
        summary="Atualizar vacina (completo)",
        description="Requer permissão de veterinário.",
        request=serializers.VacinaSerializer,
        responses={200: serializers.VacinaSerializer},
    )

    partial_update = extend_schema(
        summary="Atualizar vacina (parcial)",
        description="Requer permissão de veterinário.",
        request=serializers.VacinaSerializer,
        responses={200: serializers.VacinaSerializer},
    )

    destroy = extend_schema(
        summary="Deletar vacina",
        description="Requer permissão de veterinário.",
        responses={204: None},
    )


class RegistroVacinaSchema:
    list = extend_schema(
        summary="Listagem de registros de vacinação",
        description="""
        Lista registros de vacinação aplicadas em pets.
        
        Filtros:
        - `pet`: ID do pet para filtrar registros
        - `veterinario`: ID do veterinário para filtrar registros
        
        Regras de acesso:
        - Veterinários: visualizam todos os registros
        - Tutores: visualizam apenas registros de seus pets
        """,
        parameters=[
            OpenApiParameter(
                "pet",
                int,
                OpenApiParameter.QUERY,
                description="Filtrar registros por ID do pet",
                required=False,
            ),
            OpenApiParameter(
                "veterinario",
                int,
                OpenApiParameter.QUERY,
                description="Filtrar registros por ID do veterinário",
                required=False,
            ),
        ],
        responses={200: serializers.RegistroVacinaListSerializer(many=True)},
    )

    create = extend_schema(
        summary="Registrar vacinação",
        description="Cria um novo registro de vacinação aplicada em um pet. Requer permissão de veterinário ou tutor.",
        request=serializers.RegistroVacinaCreateSerializer,
        responses=serializers.RegistroVacinaDetailsSerializer,
    )

    retrieve = extend_schema(
        summary="Obter detalhes do registro de vacinação",
        description="Retorna informações detalhadas de um registro de vacinação específico.",
        request=serializers.RegistroVacinaCreateSerializer,
    )

    update = extend_schema(
        summary="Atualizar registro de vacinação (completo)",
        description="Requer permissão de veterinário ou tutor.",
        request=serializers.RegistroVacinaCreateSerializer,
    )

    partial_update = extend_schema(
        summary="Atualizar registro de vacinação (parcial)",
        description="Requer permissão de veterinário ou tutor.",
        request=serializers.RegistroVacinaCreateSerializer,
    )

    destroy = extend_schema(
        summary="Deletar registro de vacinação",
        description="Requer permissão de veterinário ou tutor.",
        responses={204: None},
    )
