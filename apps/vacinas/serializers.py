from rest_framework.serializers import ModelSerializer

from apps.pets.serializers import PetBasicSerializer, PetSemTutorSerializer
from apps.veterinarios.serializers import VeterinarioBasicSerializer

from .models import RegistroVacina, Vacina


class VacinaSerializer(ModelSerializer):
    class Meta:
        model = Vacina
        fields = ["id", "nome"]


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
