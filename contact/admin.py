from django.contrib import admin
from .models import Messages


class MessagesAdmin(admin.ModelAdmin):

    fields = ('first_name', 'last_name', 'email', 'subject', 'message')

    list_display = ('first_name', 'last_name', 'email', 'subject')


admin.site.register(Messages, MessagesAdmin)
