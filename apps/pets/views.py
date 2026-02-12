from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.permissions import IsVeterinario, IsVeterinarioOrTutor
from apps.tutores.models import Tutor

from . import serializers
from .models import Pet


class PetViewSet(ModelViewSet):
    def get_permissions(self):
        if self.action == "destroy":
            return [IsAdminUser()]

        if self.action in ["partial_update", "update"]:
            return [IsVeterinario()]

        return [IsVeterinarioOrTutor()]

    """
    É possível filtar os pets por tutor através de query params.
    Caso o usuário seja um tutor mas não veterinário, esse endpoint retorna somente
    os pets do usuário em si.
    """

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
