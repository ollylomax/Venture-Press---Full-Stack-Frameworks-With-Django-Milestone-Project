from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('orders/', views.order_history, name='order_history'),
    path('past_order/<order_number>', views.past_order, name='past_order'),
]