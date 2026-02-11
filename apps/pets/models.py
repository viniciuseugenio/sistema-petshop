from django.db import models
from apps.tutores.models import Tutor


class Pet(models.Model):
    nome = models.CharField(max_length=100)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name="pets")
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    sexo = models.CharField(
        max_length=1,
        choices=(("M", "Macho"), ("F", "Fêmea"), ("N", "Não Informado")),
        default="N",
    )

    def __str__(self):
        return f"{self.nome} de {self.tutor}"
