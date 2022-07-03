from django.contrib import admin
from .models import Artwork


class ArtworkAdmin(admin.ModelAdmin):

    fields = ('user', 'order', 'upload',)

    list_display = ('user', 'order', 'upload',)


admin.site.register(Artwork, ArtworkAdmin)