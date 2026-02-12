from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.permissions import IsVeterinario, IsVeterinarioOrTutor

from .models import RegistroVacina, Vacina
from .serializers import (
    RegistroVacinaDetailsSerializer,
    RegistroVacinaListSerializer,
    VacinaSerializer,
)


@extend_schema(tags=["vacinas"])
class VacinaViewSet(ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer
    permission_classes = [IsAuthenticated, IsVeterinario]


@extend_schema(tags=["registros"])
class RegistroVacinaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsVeterinarioOrTutor]

    def get_queryset(self):
        queryset = RegistroVacina.objects.select_related(
            "veterinario__user", "vacina", "pet__tutor__user"
        )

        pet_id = self.request.query_params.get("pet")
        veterinario_id = self.request.query_params.get("veterinario")

        if pet_id:
            queryset = queryset.filter(pet__id=pet_id)

        if veterinario_id:
            queryset = queryset.filter(veterinario__id=veterinario_id)

        user = self.request.user
        if user.groups.filter(name="veterinarios").exists():
            return queryset

        return queryset.filter(pet__tutor__user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return RegistroVacinaListSerializer

        return RegistroVacinaDetailsSerializer
