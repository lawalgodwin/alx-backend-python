from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="replies")

    def get_threaded_replies(self):
        """Recursively fetch a message, its replies and replies to the replies"""
        # fetch immediate replies
        replies = self.replies.all().select_related("sender", "receiver").prefetch_related("replies")
        # fetch replies for each reply
        threaded_replies = []
        for reply in replies:
            threaded_replies.append({
                "message": reply,
                replies: self.get_threaded_replies()
            })
        return threaded_replies



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="notifications")
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)


class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="history")
    old_content = models.TimeField()
    # edited_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="history")
    edited_at = models.DateTimeField(auto_now_add=True)
