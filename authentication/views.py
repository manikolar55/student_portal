from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import generics, status
from rest_framework.decorators import authentication_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password

from rest_framework.views import APIView

from django_practice.custom_backend import CustomTokenBackend, CustomTokenBackendLogout
from .models import CustomUser
from .serializers import UserSerializer
import secrets



class SignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
            Create a new user.

            This method handles the creation of a new user by receiving and validating the user data
            sent through the request. If the provided data is valid, a new user will be created, and
            authentication tokens (refresh and access tokens) will be generated for the newly created user.

            Parameters:
            ----------
            request : rest_framework.request.Request
                The HTTP request containing the user data to be used for creating the user.

            Returns:
            --------
            rest_framework.response.Response
                A response containing the result of the user creation and authentication tokens.

            Response Data (HTTP 201 Created):
            ---------------------------------
            {
                'message': 'User created successfully',
                'refresh': 'refresh_token_value_here',
                'access': 'access_token_value_here'
            }

            Response Data (HTTP 400 Bad Request):
            ------------------------------------
            {
                'field_name': ['error_message', ...],
                ...
            }
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)  # Generate token for the newly created user
            return Response({
                'message': 'User created successfully',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserLogin(APIView):
    def post(self, request):
        data = request.data
        try:
            user = CustomUser.objects.get(email=data["email"])
        except CustomUser.DoesNotExist:
            return Response(data={"message": "This email is not registered: {}".format(data["email"])},
                             status=status.HTTP_404_NOT_FOUND)

        # Check if the provided password matches the hashed password
        if not check_password(data["password"], user.password):
            return Response(data={"message": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)

        # If the login is successful, generate and save the token
        token = secrets.token_hex(32)
        user.token = token
        user.save(update_fields=["token"])

        return Response(data={"message": "Login successful!", "token": user.token}, status=status.HTTP_200_OK)


@authentication_classes([CustomTokenBackendLogout])
class CustomUserLogout(APIView):
    def post(self, request):
        return Response(data={"message": "Logout successful!"}, status=status.HTTP_200_OK)
