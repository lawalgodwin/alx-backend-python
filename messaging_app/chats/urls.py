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

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(conversation_router.urls))
]
