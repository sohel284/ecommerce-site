from django.db import models
from django.conf import settings

from app_shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, )
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return f'{self.item} * {self.quantity}'
    def get_total(self):
        total = format(self.item.price * self.quantity, '0.2f')
        return total 

class Order(models.Model):
    order_items = models.ManyToManyField(Cart, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    ordered = models.BooleanField(default=False, )
    created_at = models.DateTimeField(auto_now_add=True, )
    paymentId = models.CharField(max_length=264, null=True, blank=True, )
    orderId = models.CharField(max_length=264, null=True, blank=True, )
    
    def get_totals(self):
        totals = 0
        print(self.order_items)
        for order_item in self.order_items.all():
            value = float(order_item.get_total())
            totals = value + totals
            print(totals)
        return totals
        

