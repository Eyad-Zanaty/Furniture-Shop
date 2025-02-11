from rest_framework import serializers
from Home.models import Products, Comments, Rebly, Rating, Cart, Profile

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields= "__all__"
        
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comments
        fields= "__all__"
        
class ReblySerializer(serializers.ModelSerializer):
    class Meta:
        model=  Rebly
        fields= "__all__"
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rating
        fields= "__all__"
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cart
        fields= "__all__"
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields= "__all__"