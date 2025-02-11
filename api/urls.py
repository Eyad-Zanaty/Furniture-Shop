from django.urls import path
from . import api

app_name = 'api'
urlpatterns = [
    path('products/<int:pk>', api.ProductsList.as_view()),
    path('products/comments/<int:pk>', api.CommentsList.as_view()),
    path('products/comments/replies/<int:pk>', api.ReblyList.as_view()),
    path('products/rating/<int:pk>', api.RatingList.as_view()),
    path('cart/<int:pk>', api.CartList.as_view()),
    path('profile/<int:pk>', api.ProfileList.as_view()),
]