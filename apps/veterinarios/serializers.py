from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers

from apps.accounts.serializers import UserBasicSerializer, UserSerializer
from apps.serializers_utils import PerfilCreateSerializer

from . import models


LIST_FIELDS = ["id", "user", "celular", "crmv", "cpf"]


@extend_schema_serializer(exclude_fields=("id", "user"))
class VeterinarioSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Veterinario
        fields = LIST_FIELDS


class VeterinarioBasicSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer(read_only=True)

    class Meta:
        model = models.Veterinario
        fields = LIST_FIELDS


class VeterinarioCreateSerializer(PerfilCreateSerializer):
    crmv = serializers.CharField(max_length=20)

    def validate(self, data):
        return self._generic_validate(data, "veterinarios")

    def create(self, validated_data):
        celular = validated_data.pop("celular")
        crmv = validated_data.pop("crmv")

        user = self._get_or_create_user(validated_data, "veterinarios")
        veterinario = models.Veterinario.objects.create(
            user=user, celular=celular, crmv=crmv
        )
        return veterinario

    def to_representation(self, instance):
        return VeterinarioSerializer(instance).data
