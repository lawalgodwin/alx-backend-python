from django.db import models
from .models import Message


class UnreadMessagesManager(models.Manager):
    def get_queryset(self):
        queryset = super().get_queryset().filter(read=False).only("id", "sender", "timestamp", "content")
        return queryset