from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.permissions import IsVeterinario, IsVetHimself
from apps.veterinarios.schemas import VeterinarioSchema

from . import models, serializers


@extend_schema_view(**VeterinarioSchema.__dict__)
@extend_schema(tags=["veterinarios"])
class VeterinarioViewSet(ModelViewSet):
    queryset = models.Veterinario.objects.select_related("user")

    def get_permissions(self):
        if self.action in ["partial_update", "update"]:
            return [IsAuthenticated(), IsVetHimself()]

        if self.action in ["destroy", "create"]:
            return [IsAuthenticated(), IsAdminUser()]

        return [IsAuthenticated(), IsVeterinario()]

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.VeterinarioCreateSerializer

        return serializers.VeterinarioSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        output_serializer = serializers.VeterinarioSerializer(instance)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
