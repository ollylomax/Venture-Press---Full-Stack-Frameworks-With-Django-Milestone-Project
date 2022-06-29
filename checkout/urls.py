from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checked_out/<order_number>/', views.checked_out, name='checked_out'),
    path('webhook/', webhook, name='webhook'),
]
