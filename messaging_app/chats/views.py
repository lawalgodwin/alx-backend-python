from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import IsMessageSender
from .filters import MessageFilter


class ConversationViewSet(viewsets.ModelViewSet):
    """ A viewset for listing and performing CRUD operation
        on the conversation model
    """
    queryset = Conversation.objects.select_related('owner')
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ["owner__first_name", "owner__last_name"]
    # permission_classes = [IsParticipantOfConversation]


    def get_queryset(self):
        """Get only the conversations the user participates in"""
        qs = super().get_queryset()
        return qs.filter(participants_id=self.request.user)

    
    def perform_create(self, serializer):
        # print(serializer)
        serializer.save(owner=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    """ A viewset for listing and performing CRUD operation
        on the message model
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsMessageSender]
    filter_backends = (DjangoFilterBackend,)
    filterset_class= MessageFilter

    def get_queryset(self):
        """Get only the messages in a conversation a user participates in"""
        qs = super().get_queryset()
        return qs.filter(conversation_id__participants_id=self.request.user)

    def perform_create(self, serializer):
        conversation_id = self.kwargs["conversation_pk"]
        conversation = get_object_or_404(Conversation, pk=conversation_id)
        serializer.save(sender_id=self.request.user, conversation_id=conversation)
