from rest_framework import viewsets, status
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['post'])
    def add_semester(self, request):
        data = request.data
        serializer = SemesterSerializer(data=data)  # Use 'data' instead of 'request.data'
        if serializer.is_valid():
            serializer.save()  # Save the validated data
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)  # Use HTTP_201_CREATED for POST
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_semester(self, request):
        data = Semester.objects.select_related("section").get(id=1)

        if data is not None:
            res = {
                "name": data.section.name
            }
            return Response(res, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No data found"}, status=status.HTTP_404_NOT_FOUND)