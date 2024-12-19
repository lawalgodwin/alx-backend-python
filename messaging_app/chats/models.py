import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ The user Model an extension of the Abstract user for
        values not defined in the built-in Django User model
    """

    class Role(models.TextChoices):
        GUEST = "guest"
        HOST = "host"
        ADMIN = "admin"
    
   
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(default=None, max_length=100)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(choices=Role, default=Role.GUEST, max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "password_hash", "phone_number"]


class Message(models.Model):
    """ The message model containing the sender, conversation as
        defined in the shared schema attached to this project
    """
    message_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    sender_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="sender")
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    """  The conversation model tracks which users are involved in a conversation """
    conversation_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    participants_id = models.ForeignKey(User, related_name="participants", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)