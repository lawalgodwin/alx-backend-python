from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Message, Notification

# Create your tests here.
User = get_user_model()

class MessagingTests(TestCase):
    """Test case for the messaging app"""

    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")
    
    def test_notification_triggered_on_message_creation(self):
        message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hi Godwin")

        is_user_notified = Notification.objects.filter(user=self.user2, message=message).exists()
        self.assertTrue(is_user_notified)