from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import RegistroVacina, Vacina
from .serializers import RegistroVacinaSerializer, VacinaSerializer


class VacinaViewSet(ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer


class RegistroVacinaViewSet(ModelViewSet):
    queryset = RegistroVacina.objects.all()
    serializer_class = RegistroVacinaSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        pet_id = request.query_params.get("pet")

        if pet_id:
            queryset = queryset.filter(pet__id=pet_id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
