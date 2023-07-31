from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import StudentView, SemesterView

router = DefaultRouter()
router.register(r'student', StudentView)
router.register(r'semester', SemesterView)

urlpatterns = [
    path('', include(router.urls)),
]
