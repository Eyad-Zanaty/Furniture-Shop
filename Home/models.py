import heapq
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Products(models.Model):
    name= models.CharField(max_length= 25)
    image= models.ImageField(upload_to='products/')
    price= models.DecimalField(max_digits=6, decimal_places=2)
    orders= models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
    @staticmethod
    def get_largest_orders(n):
        return Products.objects.all().order_by('-orders')[:n]

class Cart(models.Model):
    product= models.ForeignKey(Products, on_delete=models.PROTECT)
    number= models.IntegerField(default= 1)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.product)
class Profile(models.Model):
    name= models.ForeignKey(User, on_delete=models.PROTECT)
    carts= models.ManyToManyField(Cart, blank=True)
    
    def __str__(self):
        return str(self.name)