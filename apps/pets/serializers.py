from rest_framework import serializers

from apps.tutores.models import Tutor
from apps.tutores.serializers import TutorSerializer
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    tutor = TutorSerializer()

    class Meta:
        model = Pet
        fields = ["id", "nome", "tutor", "especie", "raca", "data_nascimento"]


class PetCreateSerializer(serializers.ModelSerializer):
    tutor = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all())

    class Meta:
        model = Pet
        fields = ["id", "nome", "tutor", "especie", "raca", "data_nascimento"]
