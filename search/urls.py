from django.urls import path, include

from ecommerce.views import ProductList

from . import views


urlpatterns = [
    path('', views.SearchProduct.as_view(), name='search'),
]