
from django.contrib import admin
from django.urls import path, include

from products.views import ProductList, product_list_view

urlpatterns = [
    path('product', ProductList.as_view())
]