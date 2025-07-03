from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from users.models import User
from rest_framework.exceptions import AuthenticationFailed

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token=request.headers.get("jwt-auth")

        if not token:
            return None

        try:
            decoded=jwt.decode(token,
                               settings.SECRET_KEY,
                               algorithms=["HS256"])

            user_id=decoded["id"]
            user=User.objects.get(id=user_id)

            return (user,None)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.DecodeError:
            raise AuthenticationFailed("Error decoding token")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")