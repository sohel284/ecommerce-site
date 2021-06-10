from django.urls import path
from app_shop.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/<pk>', ProductDetail.as_view(), name='product_detail'),

]