from datetime import timedelta
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.utils import get_max_age

from .serializers import UserSerializer, UserWGroupsSerializer


# Create your views here.
class AccountsList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserWGroupsSerializer


class CustomTokenObtainPairView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response(
                {"detail": "As credenciais enviadas estão incorretas"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        access_max_age = get_max_age("ACCESS_TOKEN_LIFETIME")
        refresh_max_age = get_max_age("REFRESH_TOKEN_LIFETIME")

        refresh = RefreshToken.for_user(user)
        response = Response(
            {
                "detail": "Você está autenticado com sucesso.",
                "user": UserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )

        response.set_cookie(
            key="access_token",
            value=str(refresh.access_token),
            max_age=access_max_age,
            secure=True,
            httponly=True,
        )
        response.set_cookie(
            key="refresh_token",
            value=str(refresh),
            max_age=refresh_max_age,
            secure=True,
            httponly=True,
        )

        return response
