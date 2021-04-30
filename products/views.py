from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Product

from django.http import Http404

class ProductList(ListView):
    model = Product

class ProductDetailView(DetailView):
    template_name = 'products/product_list.html'

    def get_context_data(self, *args, **kwargs):
            context = super(ProductDetailView, self).get_context_data(**kwargs)
            print(context)
            return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("There is no such page")
        return instance
        