from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

products_colors= [
    ("Red", "Red"),
    ("Orange", "Orange"),
    ("Yellow", "Yellow"),
    ("Black", "Black"),
    ("White", "White"),
    ("Blue", "Blue"),
]

quality= [
    ("yes","yes"),
    ("no", "no")
]

when_packeting= [
    ("Without touch of hand","Without touch of hand"),
    ("With touch of hand", "With touch of hand")
]

class Rating(models.Model):
    name= models.CharField(max_length=50)
    rate= models.TextField(max_length=500)
class Rebly(models.Model):
    name= models.CharField(max_length=25)
    time= models.DateTimeField(auto_now_add=True)
    comment= models.TextField(max_length=500)

class Comments(models.Model):
    name= models.CharField(max_length=25)
    time= models.DateTimeField(auto_now_add=True)
    comment= models.TextField(max_length=500)
    reply= models.ForeignKey(Rebly, on_delete=models.CASCADE, blank=True, null=True)

class Products(models.Model):
    name= models.CharField(max_length= 25)
    image= models.ImageField(upload_to='products/')
    price= models.DecimalField(max_digits=6, decimal_places=2)
    orders= models.IntegerField(default=0)
    color= models.CharField(max_length=25, choices=products_colors)
    breif= models.TextField(max_length=250, blank=True, null=True)
    description= models.TextField(max_length=750, blank=True, null=True)
    width= models.IntegerField()
    height= models.IntegerField()
    depth= models.IntegerField()
    weight= models.IntegerField()
    quality_checking= models.CharField(max_length=3, choices=quality)
    freshness_duration= models.DateField(auto_now_add=True)
    packeting= models.CharField(max_length=50, choices=when_packeting)
    box_contains= models.IntegerField()
    comment= models.ManyToManyField(Comments, blank=True)
    rating= models.ManyToManyField(Rating, blank=True)
    slug= models.SlugField(blank= True, null= True)
    
    def __str__(self):
        return str(self.name)
    
    @staticmethod
    def get_largest_orders(n):
        return Products.objects.all().order_by('-orders')[:n]
    
    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super(Products, self).save(*args, **kwargs)
    
    @property    
    def days(self):
        delta = (self.freshness_duration - date.today()).days
        return max(delta, 0)

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
    