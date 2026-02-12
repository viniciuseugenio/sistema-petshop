from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.utils import set_access_token, set_refresh_token

from .serializers import UserWGroupsSerializer


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

        refresh = RefreshToken.for_user(user)
        response = Response(
            {
                "detail": "Você está autenticado com sucesso.",
                "user": UserWGroupsSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )

        set_access_token(response, str(refresh.access_token))
        set_refresh_token(response, str(refresh))

        return response


class CustomTokenRefreshView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response(
                {"detail": "O token não foi enviado"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        try:
            refresh = RefreshToken(refresh_token)
            user_id = refresh.get("user_id")
            user = User.objects.get(id=user_id)

            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response = Response(
                UserWGroupsSerializer(user).data, status=status.HTTP_200_OK
            )

            set_access_token(response, access_token)
            set_refresh_token(response, refresh_token)

            return response

        except TokenError:
            return Response(
                {"detail": "O token é invalido ou está expirado"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        except User.DoesNotExist:
            return Response(
                {"detail": "Este usuário não foi encontrado"},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutView(APIView):
    def post(self, request):
        response = Response({"detail": "Você foi deslogado com sucesso"})
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response
