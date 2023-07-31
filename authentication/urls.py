from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', CustomUserLogin.as_view(), name='signin'),
    path('logout/', CustomUserLogout.as_view(), name='logout'),
    # path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # For obtaining tokens
]
