from django.contrib.auth.models import Group, User
from django.db.models import Q
from rest_framework import serializers

from apps.accounts.serializers import UserBasicSerializer, UserSerializer
from apps.serializers_utils import PerfilCreateSerializer

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


class VeterinarioCreateSerializer(PerfilCreateSerializer):
    def validate(self, data):
        return self._generic_validate(data, "veterinarios")

    def create(self, validated_data):
        celular = validated_data.pop("celular")
        user = self._get_or_create_user(validated_data, "veterinarios")
        veterinario = models.Veterinario.objects.create(user=user, celular=celular)
        return veterinario
