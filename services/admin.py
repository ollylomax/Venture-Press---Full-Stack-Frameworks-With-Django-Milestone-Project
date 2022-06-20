from django.contrib import admin
from .models import Category, Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'paper_size',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)