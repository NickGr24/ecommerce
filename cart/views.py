from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
from .models import Cart, CartManager

from django.http import JsonResponse


def cart_detail_api_view(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = [{'name': x.name, 'price': x.price} for x in cart_obj.products.all()]    
    cart_data = {'products': products, 'total': cart_obj.total}
    return JsonResponse(cart_data)

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj,
        'total': cart_obj.total
    }
    return render(request, "cart/cart.html", context)

def cart_update(request):
    product_id = request.POST.get('product_id')
    
    if product_id is not None:
        product_obj = Product.objects.get(id=product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            product_added = False
        else:
            cart_obj.products.add(product_obj)
            product_added = True
        request.session['cart_items'] = cart_obj.products.count()
        if request.is_ajax():
            json_data = {
                'added': product_added,
                'removed': not product_added,
                'cartItemCount': cart_obj.products.count()
            }
            return JsonResponse(json_data)
    return redirect(cart_home)