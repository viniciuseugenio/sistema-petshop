from django.contrib import admin
from .models import Tutor


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "celular"]
