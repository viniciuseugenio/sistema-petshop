from rest_framework import permissions

from apps.tutores.models import Tutor


class IsVeterinario(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="veterinarios").exists()


class IsVeterinarioOrTutor(permissions.BasePermission):
    def has_permission(self, request, view):
        is_veterinario = request.user.groups.filter(name="veterinarios").exists()
        if is_veterinario:
            return is_veterinario

        is_tutor = Tutor.objects.filter(user=request.user).exists()
        return is_tutor

    def has_object_permission(self, request, view, obj):
        is_veterinario = request.user.groups.filter(name="veterinarios").exists()
        if is_veterinario:
            return is_veterinario

        try:
            tutor = Tutor.objects.get(user=request.user)
            is_tutor = obj.tutor == tutor
        except Tutor.DoesNotExist:
            is_tutor = False

        return is_tutor


class IsVetOrTutorHimself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_vet = request.user.groups.filter(name="veterinarios").exists()
        if is_vet:
            return True

        tutor = Tutor.objects.get(user=request.user)
        return obj == tutor


class IsVetHimself(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        return obj.user == request.user
