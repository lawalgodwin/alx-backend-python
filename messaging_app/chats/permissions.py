from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsParticipantOfConversation(BasePermission):
    """ A permission class that allow only participants in a
    conversation to send, view, update and delete messages
    """
    def has_permission(self, request, view):
        """Ensure the user is authenticated"""
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, conversation):
        """Ensure the user has CRUD privileges on its conversations"""
        participants = conversation.participants_id.all()
        user = request.user
        return (user in participants) or (user == conversation.owner)


class IsMessageSender(BasePermission):
    """Only message sender can delete message"""
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if (request.method in SAFE_METHODS):
            return True
        return obj.sender_id == request.user