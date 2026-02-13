from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from apps.pets.serializers import PetBasicSerializer, PetSemTutorSerializer
from apps.pets.models import Pet
from apps.veterinarios.models import Veterinario
from apps.veterinarios.serializers import VeterinarioBasicSerializer

from .models import RegistroVacina, Vacina


class VacinaSerializer(ModelSerializer):
    class Meta:
        model = Vacina
        fields = ["id", "nome"]
        read_only_fields = ["id"]


class RegistroVacinaListSerializer(ModelSerializer):
    veterinario = VeterinarioBasicSerializer()
    vacina = VacinaSerializer()
    pet = PetBasicSerializer()

    class Meta:
        model = RegistroVacina
        fields = ["id", "veterinario", "vacina", "pet", "data"]


class RegistroVacinaDetailsSerializer(ModelSerializer):
    veterinario = VeterinarioBasicSerializer()
    vacina = VacinaSerializer()
    pet = PetSemTutorSerializer()

    class Meta:
        model = RegistroVacina
        fields = ["id", "veterinario", "vacina", "pet", "observacoes", "data"]


class RegistroVacinaCreateSerializer(ModelSerializer):
    veterinario = serializers.PrimaryKeyRelatedField(queryset=Veterinario.objects.all())
    vacina = serializers.PrimaryKeyRelatedField(queryset=Vacina.objects.all())
    pet = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all())

    class Meta:
        model = RegistroVacina
        fields = ["id", "veterinario", "vacina", "pet", "observacoes", "data"]
        read_only_fields = ["id"]

    def to_representation(self, instance):
        return RegistroVacinaDetailsSerializer(instance).data
