from django.contrib import admin
from .models import Messages


class MessagesAdmin(admin.ModelAdmin):

    fields = ('user', 'first_name', 'last_name', 'email', 'subject', 'message')

    list_display = ('user', 'first_name', 'last_name', 'email', 'subject')


admin.site.register(Messages, MessagesAdmin)
