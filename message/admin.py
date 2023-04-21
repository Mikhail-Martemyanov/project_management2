from django.contrib import admin

from message.models import Message


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ('author_message', 'text_message', 'create_time')


admin.site.register(Message, MessageAdmin)
