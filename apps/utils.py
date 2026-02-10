from rest_framework import serializers


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
