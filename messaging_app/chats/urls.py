from django.urls import path
from . import views


urlpatterns = [
    path("conversations/", views.ConversationViewSet.as_view({ "post": "create", "get": "list" }), name="conversations"),
    path("conversations/pk", views.ConversationViewSet.as_view({"get": "retrieve"}), name="conversations"),
    path("messages/", views.MessageViewSet.as_view({ "post": "create",  "get": "list" }), name="messages"),
    path("messages/pk", views.MessageViewSet.as_view({"get": "retrieve"}), name="messages"),
]

# conversation_create = views.ConversationViewSet.as_view({"post": "create"})
# conversation_list = views.ConversationViewSet.as_view({"get": "list"})
# conversation_retrieve = views.ConversationViewSet.as_view({"get": "retrieve"})