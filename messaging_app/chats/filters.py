from django_filters import rest_framework as filters
from .models import Message


class MessageFilter(filters.FilterSet):
    """The message filtering class"""
    conversations = filters.CharFilter(
        field_name="conversation_id__conversation_id")
    sender = filters.CharFilter(field_name="sender_id__email")
    sent_before = filters.DateTimeFilter(
        field_name="sent_at",
        lookup_expr="lte")
    sent_after = filters.DateTimeFilter(
        field_name="sent_at",
        lookup_expr="gte")

    class Meta:
        model = Message
        fields = ["conversations", "sender", "sent_before", "sent_after"]
