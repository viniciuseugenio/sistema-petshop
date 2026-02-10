from django.contrib.auth.models import Group, User
from django.db.utils import IntegrityError
from rest_framework import serializers

from apps.accounts.serializers import UserSerializer

from . import models


class VeterinarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Veterinario
        fields = ["id", "user", "celular"]


class VeterinarioCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=128, required=False)

    user_id = serializers.IntegerField(requied=False)
    celular = serializers.CharField(max_length=20)

    def validate(self, data):
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

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                if user.groups.filter(name="veterinarios"):
                    raise serializers.ValidationError(
                        {"user_id": "Este usuário já é um veterinário"}
                    )

            except User.DoesNotExist:
                raise serializers.ValidationError({"user_id": "Usuário não encontrado"})

        return data

    def create(self, validated_data):
        celular = validated_data.pop("celular")
        user_id = validated_data.pop("user_id", None)

        if user_id:
            user = User.objects.get(id=user_id)
        else:
            user = User.objects.create(**validated_data)

        veterinarios_group, created = Group.objects.get_or_create(name="veterinarios")
        user.groups.add(veterinarios_group)
        veterinario = models.Veterinario.objects.create(user=user, celular=celular)
        return veterinario
