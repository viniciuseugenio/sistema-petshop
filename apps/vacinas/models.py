from django.db import models
from apps.veterinarios.models import Veterinario
from apps.pets.models import Pet
from datetime import date


class Vacina(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome


class RegistroVacina(models.Model):
    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="vacinas",
    )
    vacina = models.ForeignKey(
        Vacina, on_delete=models.SET_NULL, null=True, blank=False
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="vacinas")
    observacoes = models.TextField(blank=True)
    data = models.DateField(default=date.today)
