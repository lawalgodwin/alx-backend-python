from django.shortcuts import get_list_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ViewSet):
    """ A viewset for listing and performing CRUD operation
        on the conversation model
    """
    def list(self, request):
        conversations = Conversation.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = Conversation.objects.all()
        conversation = get_list_or_404(queryset, pk=pk)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        data = request.data
        serializer = ConversationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ViewSet):
    """ A viewset for listing and performing CRUD operation
        on the message model
    """
    def list(self, request):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        data = request.data
        serializer = MessageSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Message.objects.all()
        message = get_list_or_404(queryset, pk=pk)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)
