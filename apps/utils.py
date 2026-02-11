from rest_framework import serializers
from django.conf import settings
from datetime import timedelta


def validate_user_with_id(data):
    user_id = data.get("user_id")
    has_user_data = all(
        key in data
        for key in ["username", "first_name", "last_name", "email", "password"]
    )

    if user_id and has_user_data:
        raise serializers.ValidationError(
            "Forneça apenas o ID do usuário ou novos dados, não ambos."
        )

    if not user_id and not has_user_data:
        raise serializers.ValidationError(
            "Forneça o ID do usuário ou dados completos para criar um novo usuário."
        )


def get_max_age(key):
    lifetime: timedelta = settings.SIMPLE_JWT[key]
    return int(lifetime.total_seconds())


def set_access_token(response, token):
    access_max_age = get_max_age("ACCESS_TOKEN_LIFETIME")

    response.set_cookie(
        key="access_token",
        value=token,
        max_age=access_max_age,
        secure=True,
        httponly=True,
    )


def set_refresh_token(response, token):
    refresh_max_age = get_max_age("REFRESH_TOKEN_LIFETIME")

    response.set_cookie(
        key="refresh_token",
        value=token,
        max_age=refresh_max_age,
        secure=True,
        httponly=True,
    )
