from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.contrib import messages
from django.db.models import Q

def all_products (request):
    """ A view to show the products page and handle sorting and searching """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search details!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products' : products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_info (request, product_id):
    """ A view to show the individual product information"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'products/product_info.html', context)
