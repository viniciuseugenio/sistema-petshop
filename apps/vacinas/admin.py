from django.contrib import admin
from .models import Vacina, RegistroVacina


@admin.register(Vacina)
class VacinaAdmin(admin.ModelAdmin):
    list_display = ["id", "nome"]


@admin.register(RegistroVacina)
class RegistroVacinaAdmin(admin.ModelAdmin):
    list_display = ["id", "veterinario", "vacina", "pet", "data"]
