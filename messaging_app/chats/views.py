from django.shortcuts import render
from rest_framework import viewsets
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """ A viewset for listing and performing CRUD operation
        on the conversation model
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """ A viewset for listing and performing CRUD operation
        on the message model
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
