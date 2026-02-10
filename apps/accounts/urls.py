from django.urls import path
from . import views

urlpatterns = [path("", views.AccountsList.as_view(), name="list")]
