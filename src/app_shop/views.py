from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView

from app_shop.models import *


class Home(ListView):
    model = Product
    template_name = 'shop_app/home.html'
    

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shop_app/product_detail.html'

