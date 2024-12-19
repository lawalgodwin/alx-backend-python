from rest_framework import serializers

from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("created_at", "password_hash",)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("sender_id", "message_body", "sent_at")


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    class Meta:
        model = Conversation
        fields = "__all__"