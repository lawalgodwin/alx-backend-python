from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
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
@api_view("GET")
@cache_page(60) # cache the result for 60 seconds
def threaded_conversation(request):
    """Get a message and its replies including the replies to each reply"""
    # fetch the root messages alone
    root_messages = Message.objects.filter(
        parent_message=None, sender=request.user
        ).select_related("sender", "receiver").prefetch_related("replies")
    threaded_data = []
    for message in root_messages:
        threaded_data.append({
            "message": message,
            "replies": message.get_threaded_replies()
        })
    return render(request, "threaded_conversation.html", {"messages": threaded_data})

@login_required
def unread_messages(request):
    """Get all unread messages for the login user"""
    unread = Message.unread.unread_for_user(request.user).only("id", "sender", "timestamp", "content")
    return JsonResponse(unread, safe=False)