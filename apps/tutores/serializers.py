from rest_framework import serializers

from apps.accounts.serializers import UserBasicSerializer, UserSerializer
from apps.serializers_utils import PerfilCreateSerializer
from apps.tutores import models


class TutorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Tutor
        fields = ["id", "user", "celular", "cpf"]
        read_only_fields = ["user"]


class TutorBasicSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer()

    class Meta:
        model = models.Tutor
        fields = ["id", "user", "celular", "cpf"]


class TutorCreateSerializer(PerfilCreateSerializer):
    def validate(self, data):
        return self._generic_validate(data, "tutores")

    def create(self, validated_data):
        celular = validated_data.pop("celular")
        user = self._get_or_create_user(validated_data, "tutores")
        tutor = models.Tutor.objects.create(user=user, celular=celular)
        return tutor

    def to_representation(self, instance):
        return TutorSerializer(instance).data
