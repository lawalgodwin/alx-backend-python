from django.shortcuts import render

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from .models import Message

User = get_user_model()

def delete_user(request, pk):
    """ A view that allows a user to delete their account """
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return HttpResponse("Account deleted successfully")

@login_required
def threaded_conversation(request):
    """Get a message and its replies including the replies to each reply"""
    # fetch the root messages alone
    root_messages = Message.objects.filter(
        parent_message=None
        ).select_related("sender", "receiver").prefetch_related("replies")
    threaded_data = []
    for message in root_messages:
        threaded_data.append({
            "message": message,
            "replies": message.get_threaded_replies()
        })
    return render(request, "threaded_conversation.html", {"messages": threaded_data})