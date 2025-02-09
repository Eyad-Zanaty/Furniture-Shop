from django.urls import path
from . import views

app_name = 'Product_Details'
urlpatterns = [
    path('<str:slug>', views.product, name='product'),
]