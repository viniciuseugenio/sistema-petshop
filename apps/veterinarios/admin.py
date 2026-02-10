from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "celular"]
