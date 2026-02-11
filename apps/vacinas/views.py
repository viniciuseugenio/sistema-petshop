from rest_framework.viewsets import ModelViewSet

from .models import RegistroVacina, Vacina
from .serializers import RegistroVacinaSerializer, VacinaSerializer


class VacinaViewSet(ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer


class RegistroVacinaViewSet(ModelViewSet):
    serializer_class = RegistroVacinaSerializer

    def get_queryset(self):
        queryset = RegistroVacina.objects.all()

        pet_id = self.request.query_params.get("pet")
        veterinario_id = self.request.query_params.get("veterinario")

        if pet_id:
            queryset = queryset.filter(pet__id=pet_id)

        if veterinario_id:
            queryset = queryset.filter(veterinario__id=veterinario_id)

        return queryset
