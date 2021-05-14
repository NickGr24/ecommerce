from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.cart_home, name='cart-home'),
    path('update', views.cart_update, name='update'),
]