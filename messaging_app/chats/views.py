from http import HTTPMethod
# from django.shortcuts import get_list_or_404
# from django_filters.rest_framework import filters
from rest_framework import filters, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """ A viewset for listing and performing CRUD operation
        on the conversation model
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    filterset_fields = ["participants_is__first_name", "participants_is__last_namel"]
    # def list(self, request):
    #     conversations = Conversation.objects.all()
    #     serializer = ConversationSerializer(conversations, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def filter_queryset(self, queryset):
        return super().get_queryset()

    @action(methods=[HTTPMethod.POST, HTTPMethod.GET], detail=True)    
    def add_message(self, request, pk=None):
        conversation = self.get_object()
        print(conversation)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        # print(serializer)
        return serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
    
    # def create(self, request):
    #     data = request.data
    #     serializer = ConversationSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageViewSet(viewsets.ModelViewSet):
    """ A viewset for listing and performing CRUD operation
        on the message model
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # def list(self, request):
    #     messages = Message.objects.all()
    #     serializer = MessageSerializer(messages, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def create(self, request):
    #     data = request.data
    #     serializer = MessageSerializer(data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def retrieve(self, request, pk=None):
    #     queryset = Message.objects.all()
    #     message = get_list_or_404(queryset, pk=pk)
    #     serializer = MessageSerializer(message)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
