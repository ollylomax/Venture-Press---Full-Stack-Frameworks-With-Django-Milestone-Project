from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_requiring_artwork, name='orders_requiring_artwork')
]