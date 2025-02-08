from django.shortcuts import render
from Home.models import Products, Cart
# Create your views here.

def category(request):
    products= Products.objects.all()
    carts= Cart.objects.all()
    top_orders = Products.get_largest_orders(5)
    context= {'products' : products, 'top_orders': top_orders, 'carts': carts}
    return render(request, 'Shop/category.html', context)