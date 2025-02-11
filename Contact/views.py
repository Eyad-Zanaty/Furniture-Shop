from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from Home.models import Cart

# Create your views here.
def contact(request):
    carts= Cart.objects.all()
    if request.method== "POST" and "contact_request" in request.POST:
        name = request.POST['name']
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        send_mail(
            f"{subject} ,Contact from {name}",
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
    
    context={'carts': carts}
    return render(request, 'Contact/contact.html', context)