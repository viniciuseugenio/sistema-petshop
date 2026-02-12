from drf_spectacular.utils import OpenApiExample, OpenApiResponse, inline_serializer
from rest_framework import serializers

from apps.accounts.serializers import UserWGroupsSerializer


class LoginSchema:
    request = inline_serializer(
        name="LoginRequest",
        fields={
            "username": serializers.CharField(),
            "password": serializers.CharField(),
        },
    )

    responses = {
        200: OpenApiResponse(
            description="Login bem sucedido",
            response=UserWGroupsSerializer,
        ),
        401: OpenApiResponse(
            description="Falha na autenticação",
            response=inline_serializer(
                name="Falha no Login", fields={"detail": serializers.CharField()}
            ),
        ),
    }

    examples = [
        OpenApiExample(
            name="Exemplo de login",
            value={"username": "davi", "password": "12alkd03."},
            request_only=True,
        )
    ]


class RefreshSchema:
    responses = {
        200: OpenApiResponse(
            response=UserWGroupsSerializer,
            description="Tokens atualizados com sucesso. Novos tokens enviados via cookies HTTPOnly.",
        ),
        401: OpenApiResponse(
            response=inline_serializer(
                name="TokenRefreshError",
                fields={
                    "detail": serializers.CharField(),
                },
            ),
        ),
    }


class LogoutSchema:
    responses = {
        200: OpenApiResponse(
            response=inline_serializer(
                name="Deslogado com sucesso",
                fields={"detail": serializers.CharField()},
            )
        )
    }
