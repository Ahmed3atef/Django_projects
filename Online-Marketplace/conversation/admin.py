from django.contrib import admin
from conversation.models import Conversation, ConversationsMessage


admin.site.register(Conversation)
admin.site.register(ConversationsMessage)
