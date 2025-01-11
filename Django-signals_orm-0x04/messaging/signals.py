from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Message, Notification


@receiver(post_save, sender=Message)
def create_notification(sender, instance: Message, created, **kwargs):
    """A signal that listens for new messages and automatically creates a
    notification for the receiving user
    """
    if created:
        Notification.objects.create(
            user = instance.receiver,
            message = instance
        )