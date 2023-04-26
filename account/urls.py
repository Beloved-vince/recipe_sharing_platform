from django.urls import path
from django import views
from . import views


urlpatterns = [
    path('sign-up/', views.register_user)
]