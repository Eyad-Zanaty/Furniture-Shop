from rest_framework import generics
from .serializers import ProductsSerializer, CommentsSerializer, ReblySerializer, RatingSerializer, CartSerializer, ProfileSerializer
from Home.models import Products, Comments, Rebly, Rating, Cart, Profile

class ProductsList(generics.ListCreateAPIView):
    queryset= Products.objects.all()
    serializer_class= ProductsSerializer
    
class CommentsList(generics.ListCreateAPIView):
    queryset= Comments.objects.all()
    serializer_class= CommentsSerializer
    
class ReblyList(generics.ListCreateAPIView):
    queryset= Rebly.objects.all()
    serializer_class= ReblySerializer

class RatingList(generics.ListCreateAPIView):
    queryset= Rating.objects.all()
    serializer_class= RatingSerializer

class CartList(generics.ListCreateAPIView):
    queryset= Cart.objects.all()
    serializer_class= CartSerializer
    
class ProfileList(generics.ListCreateAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileSerializer