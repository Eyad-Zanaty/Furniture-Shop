from django.shortcuts import redirect, render
from Home.models import Products, Cart
from .filters import ProductFilter
# Create your views here.

def category(request):
    products= Products.objects.all()
    products_filter= Products.objects.all()
    carts= Cart.objects.all()
    top_orders = Products.get_largest_orders(5)
    filter= ProductFilter(request.GET, queryset=products_filter)
    products_filter= filter.qs
    
    if request.method== "POST" and "add_to_cart" in request.POST:
        product_id= request.POST.get("add_to_cart")
        prod= Products.objects.get(id= product_id)
        cart= Cart.objects.create(
            product= prod,
            price= prod.price
        )
        return redirect('Shop:shop')

    context= {"products_filter": products_filter,'products' : products, 'top_orders': top_orders, 'carts': carts, 'filter':filter}
    return render(request, 'Shop/category.html', context)