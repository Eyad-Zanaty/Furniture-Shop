from django.shortcuts import render
from Home.models import Products, Cart
from .forms import RatingForm

# Create your views here.
def product(request, slug):
    prod= Products.objects.get(slug=slug)
    
    if request.method== "POST" and 'rate' in request.POST:
        form= RatingForm(request.POST)
        if form.is_valid():
            myform= form.save(commit= True)
    else:
        form= RatingForm()
    
    context={'prod': prod, 'form': form}
    return render(request, 'Product_Details/single-product.html', context)