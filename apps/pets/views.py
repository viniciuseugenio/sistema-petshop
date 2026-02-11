from rest_framework.viewsets import ModelViewSet
from .models import Pet
from . import serializers


class PetViewSet(ModelViewSet):
    queryset = Pet.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.PetCreateSerializer

        return serializers.PetSerializer
