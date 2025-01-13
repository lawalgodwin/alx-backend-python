from django.db import models
from .models import Message


class UnreadMessagesManager(models.Manager):
    def unread_for_user(self, user):
        
        return self.filter(receiver=user, read=False).only("id", "sender", "timestamp", "content")