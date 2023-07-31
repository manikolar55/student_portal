from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from authentication.models import CustomUser


class CustomTokenBackend(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            raise AuthenticationFailed('Token should not be None')

        try:
            # Extract the token value (remove "Token " from the beginning)
            token = token.split(' ')[1]
            user = CustomUser.objects.get(token=token)
            return (user, None)  # Return a user and no credentials if authentication succeeds
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None


class CustomTokenBackendLogout(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')

        if not token:
            raise AuthenticationFailed('Token should not be None')

        try:
            # Extract the token value (remove "Token " from the beginning)
            token = token.split(' ')[1]
            user = CustomUser.objects.get(token=token)
            user.token = None
            user.save(update_fields=["token"])
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

