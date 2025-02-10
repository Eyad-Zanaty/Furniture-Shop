from django.shortcuts import redirect, render
from Home.models import Products, Cart
from .forms import CommentsForm, RatingForm

# Create your views here.
def product(request, slug):
    prod= Products.objects.get(slug=slug)
    carts= Cart.objects.all()
    top_orders = Products.get_largest_orders(5)
    
    if request.method== "POST" and "add_to_cart" in request.POST:
        num= request.POST.get("cart_number")
        product_id= request.POST.get("add_to_cart")
        product_cart= Products.objects.get(id= product_id)
        cart= Cart.objects.create(
            product= product_cart,
            number= num,
            price= prod.price,
        )
        return redirect('Product_Details:product', slug=slug)
    
    if request.method== "POST" and "submit_comment" in request.POST:
        comment_form= CommentsForm(request.POST)
        if comment_form.is_valid():
            mycomment_form = comment_form.save(commit=False)
            mycomment_form.save() 
            prod.comment.add(mycomment_form)
    else:
        comment_form= CommentsForm()
    
    if request.method== "POST" and 'submit_button' in request.POST:
        form= RatingForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.save() 
            prod.rating.add(myform)
    else:
        form= RatingForm()
    
    context={'prod': prod, 'carts': carts, 'top_orders': top_orders,'form': form, 'comment_form': comment_form }
    return render(request, 'Product_Details/single-product.html', context)