from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Message, Notification, MessageHistory

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
    
class MessageHistoryTest(TestCase):
    """Test for logs of changes made to a message"""
    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")
        self.message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Original content")

    def test_message_history_is_tracked(self):
        self.assertFalse(self.message.edited)
        # change the content
        self.message.content = "Changed Content"
        self.message.save()
        self.assertNotEqual(self.message.content, "Original content")
        # check if the changes are logged to history
        history = MessageHistory.objects.get(message=self.message)
        self.assertEqual(history.old_content, "Original content")
        self.assertTrue(self.message.edited)

