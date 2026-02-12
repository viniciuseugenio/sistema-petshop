from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.permissions import (
    IsVetOrTutorHimself,
    IsVeterinario,
)
from apps.tutores.schemas import TutorSchema

from . import serializers
from .models import Tutor


@extend_schema_view(**TutorSchema.__dict__)
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

        return serializers.TutorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        output_serializer = serializers.TutorSerializer(instance)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
