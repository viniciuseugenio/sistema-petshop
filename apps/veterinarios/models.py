from django.db import models
from django.contrib.auth.models import User


class Veterinario(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="veterinario"
    )
    celular = models.CharField(max_length=20)
