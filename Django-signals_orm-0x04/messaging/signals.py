from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory


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

@receiver(pre_save, sender=Message)
def log_to_message_edit_history(sender, instance: Message, **kwargs):
    """log the old content of a message into a separate MessageHistory model
    before it’s updated
    """
    if instance.pk:# check if the message already exists
        old_message = Message.objects.get(pk=instance.pk)
        if old_message.content != instance.content:
            MessageHistory.objects.create(
                message = instance,
                old_content = old_message.content
            )
        # mark the message as edited
        instance.edited = True
