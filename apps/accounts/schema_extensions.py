from drf_spectacular.extensions import OpenApiAuthenticationExtension


class JWTCookieAuthenticationExtension(OpenApiAuthenticationExtension):
    target_class = "apps.accounts.authentication.JWTAuthentication"
    name = "cookieAuth"

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey",
            "in": "cookie",
            "name": "access_token",
            "description": (
                "Autenticação via JWT armazenado em cookies HTTPOnly. "
                "Faça login em `/api/v1/token/` para obter os tokens automaticamente."
            ),
        }
