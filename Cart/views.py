from django.shortcuts import render
from Home.models import Cart
# Create your views here.

def cart(request):
    carts= Cart.objects.all()
    total_price= 0
    for item in carts:
        item.total_price = item.number * item.product.price 
        total_price = total_price + item.product.price * item.number 
    context= {'carts': carts, 'total_price': total_price}
    return render(request, "Cart/cart.html", context)