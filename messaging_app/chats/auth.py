from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserCreateSerializer


class UserRegisterViewSet(generics.CreateAPIView):
    """User registration view"""
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]
