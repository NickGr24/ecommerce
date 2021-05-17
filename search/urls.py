from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.SearchProduct.as_view(), name='search'),
]