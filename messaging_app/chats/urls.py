from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(
    "conversations",
    views.ConversationViewSet,
    basename="conversations"
)

router.register(
    "messages",
    views.MessageViewSet,
    basename="messages"
)


# urlpatterns = [
#     path("conversations/", views.ConversationViewSet.as_view({ "post": "create", "get": "list" }), name="conversations"),
#     path("conversations/pk", views.ConversationViewSet.as_view({"get": "retrieve"}), name="conversations"),
#     path("messages/", views.MessageViewSet.as_view({ "post": "create",  "get": "list" }), name="messages"),
#     path("messages/pk", views.MessageViewSet.as_view({"get": "retrieve"}), name="messages"),
# ]

urlpatterns = [
    path("", include(router.urls))
]

# conversation_create = views.ConversationViewSet.as_view({"post": "create"})
# conversation_list = views.ConversationViewSet.as_view({"get": "list"})
# conversation_retrieve = views.ConversationViewSet.as_view({"get": "retrieve"})