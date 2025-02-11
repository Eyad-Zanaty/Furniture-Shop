from django.shortcuts import render
from Home.models import Cart
# Create your views here.

def cart(request):
    carts= Cart.objects.all()
    
    context= {'carts': carts}
    return render(request, "Cart/cart.html", context)