from django.shortcuts import render
from django.http import HttpResponse
from .models import Cart
from django.db.models.signals import pre_save, post_save

def cart_create(user=None):
    print('New cart created')
    cart_obj = Cart.objects.create(user=None)
    return cart_obj 


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request, id=cart_obj.id)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    print(total)

    return render(request, "cart/cart.html", {'total':total})
