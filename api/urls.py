from django.urls import path
from . import api

app_name = 'api'
urlpatterns = [
    path('products', api.ProductsList.as_view()),
    path('products/lommentslist', api.CommentsList.as_view()),
    path('products/comments/reblylist', api.ReblyList.as_view()),
    path('products/ratinglist', api.RatingList.as_view()),
    path('cart', api.CartList.as_view()),
    path('profile', api.ProfileList.as_view()),
]