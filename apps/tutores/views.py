from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.permissions import (
    IsVeterinario,
    IsVetOrTutorHimself,
)
from apps.tutores.schemas import TutorSchema

from . import serializers
from .models import Tutor


@extend_schema_view(
    list=TutorSchema.list,
    create=TutorSchema.create,
    retrieve=TutorSchema.retrieve,
    update=TutorSchema.update,
    partial_update=TutorSchema.partial_update,
    destroy=TutorSchema.destroy,
)
@extend_schema(tags=["tutores"])
class TutorViewSet(ModelViewSet):
    queryset = Tutor.objects.select_related("user")

    def get_permissions(self):
        if self.action == "retrieve":
            return [IsAuthenticated(), IsVetOrTutorHimself()]

        return [IsAuthenticated(), IsVeterinario()]

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.TutorCreateSerializer

        if self.action == "list":
            return serializers.TutorBasicSerializer

        return serializers.TutorSerializer
