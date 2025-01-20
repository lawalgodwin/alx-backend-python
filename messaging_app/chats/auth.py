from rest_framework import generics
from .serializers import UserCreateSerializer


class UserRegisterViewSet(generics.CreateAPIView):
    """User registration view"""
    serializer_class = UserCreateSerializer