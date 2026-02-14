from django.contrib.auth.models import User
from django.db import models


class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="tutor")
    celular = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True, null=True)

    def __str__(self):
        return f"Tutor {self.user.username}"

    class Meta:
        ordering = ["-id"]
        verbose_name = "Tutor"
        verbose_name_plural = "Tutores"
