from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

#models
from app_shop.models import *
from app_order.models import *

@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    print(item)
    order_item = Cart.objects.get_or_create(item=item, user=request.user)
    print('Order Item')
    print(order_item)
    print(order_item[0])
    print(order_item[0].user)
    order_qs = Order.objects.filter(user=request.user, ordered=False, )
    print(order_qs)
    if order_qs.exists():
        order = order_qs[0]
        print(order)
        if order.order_items.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            print(order_item[0])
            messages.info(request, "This item quantity was upadted")
            return redirect('home')
        else:
            print(order_item[0])
            order.order_items.add(order_item[0])
            print(order.order_items)
            messages.info(request, "this item was added to your cart")
            return redirect('home')
    else:
        order = Order(user=request.user)
        order.save()
        order.order_items.add(order_item[0])
        messages.info(request, "This item was added to your cart")
        return redirect('home')

@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, purchased=False, )
    orders = Order.objects.filter(user=request.user, ordered=False, )
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'order_app/cart.html', {
            'carts':carts,
            'order': order,
        })
    else:
        messages.warning(request, "You don't have any item in cart")
        return redirect('home')

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    print(item)
    order_qs = Order.objects.filter(user=request.user, ordered=False, )
    if order_qs.exists():
        order = order_qs[0]
        print(order)
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.filter(user=request.user, item=item, purchased=False, )[0]
            order.order_items.remove(order_item)
            order_item.delete()
            messages.warning(request, 'This item was removed your cart')
            return redirect('cart_view')
        else:
            messages.info(request, "You don't have an active order")
            return redirect('home')
    else:
        messages.info(request, "You don't have any order")
        return redirect('home')

def increase_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    print(item)
    order_qs = Order.objects.filter(user=request.user, ordered=False, )
    if order_qs.exists():
        order = order_qs[0]
        print(order)
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.filter(user=request.user, item=item, purchased=False, )[0]
            if order_item.quantity >= 1:
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f'{item.name} was update your product item')
                return redirect('cart_view')
        else:
            messages.info(request, f"{item.name} is not your cart")
            return redirect('home')
    else:
        messages.info(request, "You don't have any order")
        return redirect('home')
def decrease_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    print(item)
    order_qs = Order.objects.filter(user=request.user, ordered=False, )
    if order_qs.exists():
        order = order_qs[0]
        print(order)
        if order.order_items.filter(item=item).exists():
            order_item = Cart.objects.filter(user=request.user, item=item, purchased=False, )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request, f'{item.name} was update your item')
                return redirect('cart_view')
            else:
                order.order_items.remove(order_item)
                order_item.delete()
                messages.warning(request, f'{item.name} was removed from your cart ') 
                return redirect('home')   
        else:
            messages.info(request, f"{item.name} is not your cart")
            return redirect('home')
    else:
        messages.info(request, "You don't have any order")
        return redirect('home')        