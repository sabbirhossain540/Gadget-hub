from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product

# Create your views here.
def store(request, category_slug = None):
    
    category = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)

        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    

    context = {
        'products' : products,
        'product_count' : product_count,
    }

    return render(request, 'store/store.html', context)


def products_detail(request, category_slug, product_slug):
    return render(request, 'store/product_detail.html')
