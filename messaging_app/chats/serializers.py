from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)
    # username = serializers.CharField(source="get_email", read_only=True)
    password = serializers.CharField(source="get_password_hash", write_only=True)
    webiners = serializers.PrimaryKeyRelatedField(many=True, queryset=Conversation.objects.all())

    class Meta:
        model = User
        fields = ["user_id", "first_name", "last_name", "email", "phone_number", "password_hash", "password", "full_name", "webiners"]
    
    def validate_password_hash(self, value):
        """ Check that the length of the password is at least 8 """
        if len(value) < 8:
            raise serializers.ValidationError("Password not long enough")
        return value
    
    def create(self, **kwargs):
        password = self.validated_data["password_hash"]
        kwargs = self.validated_data
        email = self.validated_data["email"]
        account = User(email=email, **kwargs)
        account.set_password(password)
        account.save()
        return account


class MessageSerializer(serializers.ModelSerializer):
    sender_id = serializers.CharField(source="sender_id.email", read_only=True)
    conversation_id = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Message
        fields = "__all__"
        ordering = ["-sent_at"]


class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    latest_message = serializers.SerializerMethodField()
    initial_message = serializers.ReadOnlyField(source="openning_message")
    owner = serializers.ReadOnlyField(source="owner.email")


    def get_latest_message(self, obj):
        last_message = obj.messages.order_by("-sent_at").first()
        return MessageSerializer(last_message).data if last_message else None
    

    class Meta:
        model = Conversation
        fields = "__all__"
    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(user.first_name)
        # Add custom claims
        return token



class UserCreateSerializer(serializers.ModelSerializer):
    """User Create serializer"""
    password_hash = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "password_hash", "first_name", "last_name", "phone_number")
   
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
