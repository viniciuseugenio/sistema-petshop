from django.contrib.auth.models import Group, User
from rest_framework import serializers

from apps.accounts.serializers import UserBasicSerializer, UserSerializer
from apps.utils import validate_user_with_id

from . import models


class VeterinarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Veterinario
        fields = ["id", "user", "celular"]


class VeterinarioBasicSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer(read_only=True)

    class Meta:
        model = models.Veterinario
        fields = ["id", "user", "celular"]


class VeterinarioCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, required=False)
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=128, required=False)

    user_id = serializers.IntegerField(required=False)
    celular = serializers.CharField(max_length=20)

    def validate(self, data):
        validate_user_with_id(data)
        user_id = data.get("user_id")

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                if user.groups.filter(name="veterinarios").exists():
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
            user = User.objects.create_user(**validated_data)

        veterinarios_group, created = Group.objects.get_or_create(name="veterinarios")
        user.groups.add(veterinarios_group)
        veterinario = models.Veterinario.objects.create(user=user, celular=celular)
        return veterinario
