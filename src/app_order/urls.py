from django.urls import path
from app_order.views import *

urlpatterns = [
    path('add/<pk>', add_to_cart, name='add'),
    path('cart-view', cart_view, name='cart_view'),
    path('remove/<pk>', remove_from_cart, name='remove'),
    path('increase/<pk>', increase_item, name='increase_item'),
    path('decrease/<pk>', decrease_item, name='decrease_item'),
    
]