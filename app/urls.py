from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import StudentView
router = DefaultRouter()
router.register(r'student', StudentView)

urlpatterns = [
    path('', include(router.urls)),
]
