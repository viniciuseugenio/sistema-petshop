from drf_spectacular.utils import (
    OpenApiParameter,
    extend_schema,
    extend_schema_view,
)
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.permissions import IsVeterinario, IsVeterinarioOrTutor
from apps.pets.schemas import PetSchema
from apps.tutores.models import Tutor

from . import serializers
from .models import Pet


@extend_schema_view(**PetSchema.__dict__)
@extend_schema(tags=["pets"])
class PetViewSet(ModelViewSet):
    def get_permissions(self):
        if self.action == "destroy":
            return [IsAdminUser()]

        if self.action in ["partial_update", "update", "create"]:
            return [IsVeterinario()]

        return [IsVeterinarioOrTutor()]

    def get_queryset(self):
        queryset = Pet.objects.select_related("tutor", "tutor__user")
        tutor_id = self.request.query_params.get("tutor")

        if tutor_id:
            queryset = queryset.filter(tutor__id=tutor_id)

        is_vet = self.request.user.groups.filter(name="veterinarios").exists()
        if is_vet:
            return queryset

        tutor = Tutor.objects.get(user=self.request.user)
        return queryset.filter(tutor=tutor)

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.PetCreateSerializer

        if self.action == "retrieve":
            return serializers.PetDetailsSerializer

        return serializers.PetListSerializer
