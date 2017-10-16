from django.views.generic import ListView, DetailView
from technic_catalog.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'


class ProductView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'
