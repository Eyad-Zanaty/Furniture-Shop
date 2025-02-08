from django.urls import path
from . import views

app_name = 'Shop'
urlpatterns = [
    path('category', views.category, name='shop'),
]