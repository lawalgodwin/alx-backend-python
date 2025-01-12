from django.shortcuts import render

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse

User = get_user_model()

def delete_user(request, pk):
    """ A view that allows a user to delete their account """
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return HttpResponse("Account deleted successfully")
