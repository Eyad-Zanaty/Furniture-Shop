from django.shortcuts import render
from Home.models import Cart

# Create your views here.
def login(request):
    carts= Cart.objects.all()
    
    context= {'carts': carts}
    return render(request, 'Profile/login.html', context)