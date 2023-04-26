from django.urls import path
from .views import UserRegistration

urlpatterns = [
    path('sign-up/', UserRegistration.as_view(), name='user-register'),
]