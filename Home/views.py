from django.conf import settings
from django.shortcuts import redirect, render
from .models import Products, Cart, Profile
from django.core.mail import send_mail
# Create your views here.

def home(request):
    products= Products.objects.all()
    user= Profile.objects.get(name= request.user)
    top_orders = Products.get_largest_orders(5)
    carts= Cart.objects.all()
    if request.method== "POST" and "add_to_cart" in request.POST:
        product_id= request.POST.get("add_to_cart")
        prod= Products.objects.get(id= product_id)
        cart= Cart.objects.create(
            product= prod,
            price= prod.price
        )
        return redirect('Home:home')
    
    if request.method== "POST" and "discount" in request.POST:
        email = request.POST['discount']
        send_mail(
        "From Furniture Shop",
        f"You had the discount {user}",
        email,
        [settings.EMAIL_HOST_USER],
        )
    
    if request.method== "POST" and "subscribe" in request.POST:
        email = request.POST['subscribe']
        send_mail(
        "From Furniture Shop",
        f"You had subscribed {user}",
        email,
        [settings.EMAIL_HOST_USER],
        )
    context= {'products' : products, 'user': user, 'top_orders': top_orders, 'carts': carts}
    return render(request, 'Home/home.html', context)