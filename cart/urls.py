from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.cart_home, name='cart-home'),
    path('api/', views.cart_detail_api_view, name='home-cart'),
    path('update', views.cart_update, name='update'),
]