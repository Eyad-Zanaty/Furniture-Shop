from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Products, Cart, Profile
# Create your views here.

def home(request):
    products= Products.objects.all()
    user= Profile.objects.get(name= request.user)
    top_orders = Products.get_largest_orders(5)
    if request.method== "POST" and "add_to_cart" in request.POST:
        product_id= request.POST.get("add_to_cart")
        prod= Products.objects.get(id= product_id)
        cart= Cart.objects.create(
            product= prod,
            price= prod.price
        )
        return redirect('Home:home')
    
    context= {'products' : products, 'user': user, 'top_orders': top_orders}
    return render(request, 'Home/home.html', context)