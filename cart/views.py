from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Product
from .models import Cart, CartManager
from billing.models import BillingProfile
from accounts.forms import GuestForm, LoginForm
from orders.models import Order
from accounts.models import GuestEmail
from django.http import JsonResponse
from addresses.forms import AddressForm
from addresses.models import Address
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
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            json_data = {
                'added': product_added,
                'removed': not product_added,
                'cartItemCount': cart_obj.products.count()
            }
            return JsonResponse(json_data)
    return redirect(cart_home)

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect(cart_home)
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    
    guest_form = GuestForm()
    login_form = LoginForm()
    address_form = AddressForm()
    shipping_address_id = request.session.get('shipping_address_id', None)
    billing_address_form = AddressForm()
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if billing_profile is not None:
        order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
        if shipping_address_id:
            order_obj.shipping_address = shipping_address_id
            order_obj.save()
    context = {
        'object': order_obj,
        'billing_profile': billing_profile,
        'login_form': login_form,
        'guest_form': guest_form,
        'address_form': address_form,
        'billing_address_form': address_form,
    }

    return render(request, 'checkout.html', context)