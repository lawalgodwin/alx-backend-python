from django.urls import path, include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register(
    r"conversations",
    views.ConversationViewSet
)

conversation_router = routers.NestedDefaultRouter(
    router,
    r"conversations",
    lookup="conversation"
)

conversation_router.register(
    "messages",
    views.MessageViewSet,
    basename="conversations-messages"
)


# urlpatterns = [
#     path("conversations/", views.ConversationViewSet.as_view({ "post": "create", "get": "list" }), name="conversations"),
#     path("conversations/pk", views.ConversationViewSet.as_view({"get": "retrieve"}), name="conversations"),
#     path("messages/", views.MessageViewSet.as_view({ "post": "create",  "get": "list" }), name="messages"),
#     path("messages/pk", views.MessageViewSet.as_view({"get": "retrieve"}), name="messages"),
# ]

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(conversation_router.urls))
]

# conversation_create = views.ConversationViewSet.as_view({"post": "create"})
# conversation_list = views.ConversationViewSet.as_view({"get": "list"})
# conversation_retrieve = views.ConversationViewSet.as_view({"get": "retrieve"})