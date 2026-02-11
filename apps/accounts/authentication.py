from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError
from rest_framework_simplejwt.tokens import AccessToken


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        access_token = request.COOKIES.get("access_token")

        if not access_token:
            return None

        try:
            access_obj = AccessToken(access_token)
            user_id = access_obj.get("user_id")
            user = User.objects.get(id=user_id)
            return (user, None)
        except TokenError:
            raise AuthenticationFailed("Invalid or expired tokens")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")
