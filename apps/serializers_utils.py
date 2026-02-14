from rest_framework import serializers
from django.contrib.auth.models import Group, User

from apps.utils import validate_user_with_id, verify_group


class PerfilCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=128, required=False)

    user_id = serializers.IntegerField(required=False)
    cpf = serializers.CharField(max_length=11)
    celular = serializers.CharField(max_length=20)

    def _generic_validate(self, data, group_name):
        validate_user_with_id(data)
        user_id = data.get("user_id")

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                if verify_group(user, group_name):
                    raise serializers.ValidationError(
                        {"user_id": f"Este usuário já é um {group_name}"}
                    )

            except User.DoesNotExist:
                raise serializers.ValidationError({"user_id": "Usuário não encontrado"})

        return data

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Um usuário com este e-mail já existe.")

        return value

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("Um usuário com este username já existe.")

        return value

    def _get_or_create_user(self, validated_data, group_name):
        user_id = validated_data.pop("user_id", None)

        if user_id:
            user = User.objects.get(id=user_id)
        else:
            user = User.objects.create_user(**validated_data)

        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        return user
