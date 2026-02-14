from django.db import models
from django.contrib.auth.models import User


class Veterinario(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="veterinario"
    )
    celular = models.CharField(max_length=20)
    crmv = models.CharField(max_length=20, unique=True, null=True)

    def __str__(self):
        return f"Veterinário {self.user.username}"
