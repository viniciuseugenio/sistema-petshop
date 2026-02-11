from rest_framework.viewsets import ModelViewSet

from . import serializers
from .models import Pet


class PetViewSet(ModelViewSet):
    def get_queryset(self):
        queryset = Pet.objects.select_related("tutor", "tutor__user")
        tutor_id = self.request.query_params.get("tutor")

        if tutor_id:
            queryset = queryset.filter(tutor__id=tutor_id)

        return queryset

    def get_serializer_class(self):
        if self.action == "create":
            return serializers.PetCreateSerializer

        if self.action == "retrieve":
            return serializers.PetDetailsSerializer

        return serializers.PetListSerializer
