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
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    celular = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        celular = validated_data.pop("celular")

        try:
            user = User.objects.create_user(**validated_data)
            veterinario_group, created = Group.objects.get_or_create(name="veterinario")
            user.groups.add(veterinario_group)

            veterinario = models.Veterinario.objects.create(user=user, celular=celular)
            return veterinario
        except IntegrityError:
            raise serializers.ValidationError(
                {"error": "Usuário com este username ou email já existe"}
            )
