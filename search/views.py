from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class SearchProduct(ListView):
    template_name='list.html'

    def get_queryset(self, *args, **kwargs):
        return Product.objects.filter(title__icontains=self.request.GET.get('search'))