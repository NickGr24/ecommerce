from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.db.models import Q

class SearchProduct(ListView):
    template_name='view.html'
    

    def get_context_data(self, **kwargs):
        context = super(SearchProduct, self).get_context_data(**kwargs)
        query = self.request.GET.get('search')
        context['query'] = query
        return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('search', None)
        if query is not None:
            lookups = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
            return Product.objects.filter(lookups).distinct()
        return Product.objects.all()