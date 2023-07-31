from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.decorators import authentication_classes, permission_classes

from app.models import Students
from app.serializers import StudentSerializer
from django_practice.custom_backend import CustomTokenBackend


# Create your views here.

@authentication_classes([CustomTokenBackend])
class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

