from django.shortcuts import render
from Home.models import Products, Cart

# Create your views here.
def product(request, slug):
    prod= Products.objects.get(slug=slug)
    context={'prod': prod}
    return render(request, 'Product_Details/single-product.html', context)