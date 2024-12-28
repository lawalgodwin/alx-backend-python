from http import HTTPMethod
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets, views, status, generics
from rest_framework.response import Response
from .serializers import UserCreateSerializer


class UserRegisterViewSet(generics.CreateAPIView):
    """User registration view"""
    serializer_class = UserCreateSerializer