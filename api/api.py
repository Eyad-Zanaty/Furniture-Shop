from rest_framework import generics
from .serializers import ProductsSerializer, CommentsSerializer, ReblySerializer, RatingSerializer, CartSerializer, ProfileSerializer
from Home.models import Products, Comments, Rebly, Rating, Cart, Profile

class ProductsList(generics.RetrieveUpdateDestroyAPIView):
    queryset= Products.objects.all()
    serializer_class= ProductsSerializer
    
class CommentsList(generics.RetrieveUpdateDestroyAPIView):
    queryset= Comments.objects.all()
    serializer_class= CommentsSerializer
    
class ReblyList(generics.RetrieveUpdateDestroyAPIView):
    queryset= Rebly.objects.all()
    serializer_class= ReblySerializer

class RatingList(generics.RetrieveUpdateDestroyAPIView):
    queryset= Rating.objects.all()
    serializer_class= RatingSerializer

class CartList(generics.RetrieveUpdateDestroyAPIView):
    queryset= Cart.objects.all()
    serializer_class= CartSerializer
    
class ProfileList(generics.RetrieveUpdateDestroyAPIView):
    queryset= Profile.objects.all()
    serializer_class= ProfileSerializer