from django.urls import path
from .views import test_endpoint,security_stats,suspicious_ips,dashboard,custom_login
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('test/', test_endpoint),
    path('stats/',security_stats),
    path('suspicious/',suspicious_ips),
    path('dashboard/',dashboard),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('login/',custom_login),
]