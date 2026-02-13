from rest_framework import permissions

from apps.tutores.models import Tutor
from apps.utils import verify_group


class AdminBypassPermission(permissions.BasePermission):
    def _is_admin(self, user):
        return user.is_staff or user.is_superuser


class IsVeterinario(AdminBypassPermission):
    def has_permission(self, request, view):
        if self._is_admin(request.user):
            return True

        return verify_group(request.user, "veterinarios")


class IsVeterinarioOrTutor(AdminBypassPermission):
    def has_permission(self, request, view):
        if self._is_admin(request.user):
            return True

        if verify_group(request.user, "veterinarios"):
            return True

        is_tutor = Tutor.objects.filter(user=request.user).exists()
        return is_tutor

    def has_object_permission(self, request, view, obj):
        if self._is_admin(request.user):
            return True

        if verify_group(request.user, "veterinarios"):
            return True

        try:
            tutor = Tutor.objects.get(user=request.user)
            is_tutor = obj.tutor == tutor
        except Tutor.DoesNotExist:
            is_tutor = False

        return is_tutor


class IsVetOrTutorHimself(AdminBypassPermission):
    def has_object_permission(self, request, view, obj):
        if self._is_admin(request.user):
            return True

        if verify_group(request.user, "veterinarios"):
            return True

        tutor = Tutor.objects.get(user=request.user)
        return obj == tutor


class IsVetHimself(AdminBypassPermission):
    def has_object_permission(self, request, view, obj):
        if self._is_admin(request.user):
            return True

        return obj.user == request.user
