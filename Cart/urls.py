from django.urls import path
from . import views

app_name = 'Cart'
urlpatterns = [
    path('', views.cart, name='cart'),
]