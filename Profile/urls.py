from django.urls import path
from . import views

app_name = 'Profile'
urlpatterns = [
    path('login', views.login, name='login'),
]