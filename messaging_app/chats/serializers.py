from rest_framework import serializers

from chats.models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("created_at", "user_id")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("sender_id", "message_body")


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ("participants_id")