from django.urls import path

from . import views


urlpatterns = [
    path('', views.SearchProduct.as_view(), name='search'),
]