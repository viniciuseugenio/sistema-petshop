from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import UserWGroupsSerializer


# Create your views here.
class AccountsList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserWGroupsSerializer
