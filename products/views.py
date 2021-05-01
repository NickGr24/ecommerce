from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Product

from django.http import Http404

class ProductList(ListView):
    model = Product
    template_name = 'list.html'

    

class ProductDetailView(DetailView):
    template_name = 'products/product_list.html'

    def get_context_data(self, *args, **kwargs):
            context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
            return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("There is no such page")
        return instance
        
    def product_detail(request, pk):
        context = {
        'product': get_object_or_404(Product, pk=id),
        'title': 'Product Detail'
        }
        return render(request, 'detail.html', context)


