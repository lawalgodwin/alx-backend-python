from rest_framework import serializers

from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    username = serializers.CharField(source="get_email", read_only=True)
    password = serializers.CharField(source="get_password_hash", write_only=True)

    class Meta:
        model = User
        exclude = ("created_at", "password_hash",)
    
    def validate_password_hash(self, value):
        """ Check that the length of the password is at least 8 """
        if len(value) < 8:
            raise serializers.ValidationError("Password not long enough")
        return value
    
    def save(self, **kwargs):
        password = self.validated_data["password_hash"]
        kwargs = self.validated_data
        email = self.validated_data["email"]
        account = User(email=email, username=email, **kwargs)
        account.set_password(password)
        account.save()
        return account


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = "__all__"
        ordering = ["-sent_at"]


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    latest_message = serializers.SerializerMethodField()

    def get_latest_message(self, obj):
        last_message = obj.messages.order_by("-sent_at").first()
        return MessageSerializer(last_message).data if last_message else None

    class Meta:
        model = Conversation
        fields = "__all__"
