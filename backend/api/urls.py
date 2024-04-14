from django.urls import path
from . import views
from .views import TaskListCreateAPIView, PomodoroSessionListCreateAPIView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('pomo_sessions/', PomodoroSessionListCreateAPIView.as_view(), name='session-list-create'),
]