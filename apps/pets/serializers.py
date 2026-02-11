from django.db.models.base import ModelStateFieldsCacheDescriptor
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.tutores.models import Tutor
from apps.tutores.serializers import TutorBasicSerializer, TutorSerializer
from .models import Pet


class PetListSerializer(ModelSerializer):
    tutor = TutorBasicSerializer()

    class Meta:
        model = Pet
        fields = ["id", "nome", "tutor", "especie", "raca", "data_nascimento"]


class PetBasicSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "nome"]


class PetSemTutorSerializer(ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "nome", "especie", "raca", "data_nascimento"]


class PetDetailsSerializer(ModelSerializer):
    tutor = TutorSerializer()

    class Meta:
        model = Pet
        fields = ["id", "nome", "tutor", "especie", "raca", "data_nascimento"]


class PetCreateSerializer(ModelSerializer):
    tutor = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all())

    class Meta:
        model = Pet
        fields = ["id", "nome", "tutor", "especie", "raca", "data_nascimento"]
