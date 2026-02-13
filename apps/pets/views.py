from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.permissions import IsVeterinario, IsVeterinarioOrTutor
from apps.pets.schemas import PetSchema
from apps.tutores.models import Tutor
from apps.utils import verify_group

from . import serializers
from .models import Pet


@extend_schema_view(**PetSchema.__dict__)
@extend_schema(tags=["pets"])
class PetViewSet(ModelViewSet):
    queryset = Pet.objects.select_related("tutor", "tutor__user")

    def get_permissions(self):
        if self.action == "destroy":
            return [IsAuthenticated(), IsAdminUser()]

        if self.action in ["partial_update", "update", "create"]:
            return [IsAuthenticated(), IsVeterinario()]

        return [IsAuthenticated(), IsVeterinarioOrTutor()]

    def get_queryset(self):
        queryset = super().get_queryset()
        tutor_id = self.request.query_params.get("tutor")

        if tutor_id:
            queryset = queryset.filter(tutor__id=tutor_id)

        if verify_group(self.request.user, "veterinarios"):
            return queryset

        tutor = Tutor.objects.get(user=self.request.user)
        return queryset.filter(tutor=tutor)

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.PetCreateSerializer

        if self.action == "retrieve":
            return serializers.PetDetailsSerializer

        return serializers.PetListSerializer
