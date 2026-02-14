from django.db.models import ProtectedError
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.permissions import IsVeterinario, IsVeterinarioOrTutor
from apps.utils import verify_group
from apps.vacinas.schemas import RegistroVacinaSchema, VacinaSchema

from .models import RegistroVacina, Vacina
from .serializers import (
    RegistroVacinaCreateSerializer,
    RegistroVacinaDetailsSerializer,
    RegistroVacinaListSerializer,
    VacinaSerializer,
)


@extend_schema_view(
    list=VacinaSchema.list,
    create=VacinaSchema.create,
    retrieve=VacinaSchema.retrieve,
    update=VacinaSchema.update,
    partial_update=VacinaSchema.partial_update,
    destroy=VacinaSchema.destroy,
)
@extend_schema(tags=["vacinas"])
class VacinaViewSet(ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer
    permission_classes = [IsAuthenticated, IsVeterinario]

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {
                    "detail": "Não é possível deletar este objeto porque existem associações protegidas."
                },
                status=status.HTTP_409_CONFLICT,
            )


@extend_schema_view(
    list=RegistroVacinaSchema.list,
    create=RegistroVacinaSchema.create,
    retrieve=RegistroVacinaSchema.retrieve,
    update=RegistroVacinaSchema.update,
    partial_update=RegistroVacinaSchema.partial_update,
    destroy=RegistroVacinaSchema.destroy,
)
@extend_schema(tags=["registros"])
class RegistroVacinaViewSet(ModelViewSet):
    queryset = RegistroVacina.objects.select_related(
        "veterinario__user", "vacina", "pet__tutor__user"
    )
    permission_classes = [IsAuthenticated, IsVeterinarioOrTutor]

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_id = self.request.query_params.get("pet")
        veterinario_id = self.request.query_params.get("veterinario")

        if pet_id:
            queryset = queryset.filter(pet__id=pet_id)

        if veterinario_id:
            queryset = queryset.filter(veterinario__id=veterinario_id)

        user = self.request.user
        if verify_group(user, "veterinarios"):
            return queryset

        return queryset.filter(pet__tutor__user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return RegistroVacinaListSerializer

        if self.action in ["create", "update", "partial_update"]:
            return RegistroVacinaCreateSerializer

        return RegistroVacinaDetailsSerializer
