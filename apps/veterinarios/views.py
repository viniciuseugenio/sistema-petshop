from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from . import models, serializers


# Create your views here.
class VeterinarioViewSet(ModelViewSet):
    queryset = models.Veterinario.objects.select_related("user")

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
