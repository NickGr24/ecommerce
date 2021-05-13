from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_home, name='cart-home'),
    path('cart-update/', views.cart_update, name='cart-update')
]