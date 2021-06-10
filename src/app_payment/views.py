from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from app_payment.models import BillingAddress
from app_order.models import Order

from app_payment.forms import BillingForm


@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.info(request, 'Shipping Address is saved')

    order_qs = Order.objects.filter(user=request.user, ordered=False, )[0]
    print(order_qs)
    order_items = order_qs.order_items.all()
    print(order_items)
    order_total = order_qs.get_totals
    print(order_total)
    return render(request, 'payment_app/checkout.html', {'form': form, 'order_items': order_items, 'order_total': order_total})
