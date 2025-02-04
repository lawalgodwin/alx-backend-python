from django.contrib import admin
from .models import Message, Conversation, User


# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ["email", "first_name", "last_name"]
#     ordering = ["email"]

# admin.site.register(User, CustomUserAdmin)
admin.site.register(User)
admin.site.register(Conversation)
admin.site.register(Message)
