from django.shortcuts import render, redirect, get_object_or_404
from cartapp.models import Products
from .models import Bag, CartItem
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def _bag_id(request):
    bag = request.session.session_key
    if not bag:
        bag = request.session.create()
    return bag


def add_bag(request, product_id):
    product = Products.objects.get(id=product_id)
    try:
        bag = Bag.objects.get(bag_id=_bag_id(request))
    except Bag.DoesNotExist:
        bag = Bag.objects.create(bag_id=_bag_id(request))
        bag.save()
    try:
        cart_item = CartItem.objects.get(product=product, bag=bag)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, bag=bag)
        cart_item.save()
    return redirect('bag:bag_detail')


def bag_detail(request, total=0, counter=0, cart_items=None):
    try:
        bag = Bag.objects.get(bag_id=_bag_id(request))
        cart_items = CartItem.objects.filter(bag=bag, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def bag_remove(request, product_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, bag=bag)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('bag:bag_detail')


def bag_delete(request, product_id):
    bag = Bag.objects.get(bag_id=_bag_id(request))
    product = get_object_or_404(Products, id=product_id)
    cart_item = CartItem.objects.get(product=product, bag=bag)
    cart_item.delete()
    return redirect('bag:bag_detail')
