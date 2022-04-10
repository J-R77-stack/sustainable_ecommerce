from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products (request):
    """ A view to show the products page and handle sorting and searching """

    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, 'products/products.html', context)


def product_info (request):
    """ A view to show the individual product information"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_info.html', context)
