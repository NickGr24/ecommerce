from django.shortcuts import render

from django.views.generic import ListView, DetailView

from cart.models import Cart

from .models import Product

from django.http import Http404

class ProductList(ListView):
    model = Product
    template_name = 'products.html'

class ProductDetailView(DetailView):
    template_name = 'detail.html'
    queryset = Product.objects.all()

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        try:
            instance = Product.objects.get(pk=pk, active=True)
        except Product.DoesNotExist:
            raise Http404('There is no such product')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(pk=pk, active=True)
            instance = qs.first()
        return instance


    def get_context_data(self, *args, **kwargs):
            context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
            cart_obj, new_obj = Cart.objects.new_or_get(self.request)
            context['cart'] = cart_obj
            return context

        
    def product_detail(request, pk):
        context = {
        'product': get_object_or_404(Product, pk=id),
        'title': 'Product Detail'
        }
        return render(request, 'detail.html', context)


