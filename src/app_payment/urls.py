from django.urls import path

from app_payment.views import checkout

urlpatterns = [
    path('checkout', checkout, name='checkout'),
]