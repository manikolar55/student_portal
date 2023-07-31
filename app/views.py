from rest_framework import viewsets
from rest_framework.decorators import authentication_classes

from app.models import Students, Semester
from app.serializers import StudentSerializer, SemesterSerializer
from django_practice.custom_backend import CustomTokenBackend


# Create your views here.

# @authentication_classes([CustomTokenBackend])
class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


# @authentication_classes([CustomTokenBackend])
class SemesterView(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
