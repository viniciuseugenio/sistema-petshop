from rest_framework.viewsets import ModelViewSet

from .models import RegistroVacina, Vacina
from .serializers import RegistroVacinaSerializer, VacinaSerializer


class VacinaViewSet(ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer


class RegistroVacinaViewSet(ModelViewSet):
    queryset = RegistroVacina.objects.all()
    serializer_class = RegistroVacinaSerializer
