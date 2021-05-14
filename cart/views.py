from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
from .models import Cart, CartManager

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    cart_obj.total = total
    cart_obj.save()
    return render(request, "cart/cart.html")

def cart_update(request):
    print(request.POST)
    product_id =  1 #request.POST.get('product_id')
    obj = Product.objects.get(id=product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    if obj in cart_obj.products.all():
        cart_obj.products.remove(obj)
    else:
        cart_obj.products.add(obj)
    return redirect(cart_home)