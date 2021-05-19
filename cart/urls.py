from django.urls import path
from . import views
from accounts.views import guest_register_view
from addresses.views import checkout_address_create_view
urlpatterns = [
    path('home/', views.cart_home, name='cart-home'),
    path('api/', views.cart_detail_api_view, name='home-cart'),
    path('update', views.cart_update, name='update'),
    path('checkout/', views.checkout_home, name='checkout'),
    path('checkout/guest/', guest_register_view, name='guest'),
    path('checkout/address', checkout_address_create_view, name='address'),
    ]