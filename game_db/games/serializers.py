from rest_framework import serializers
from .models import Category, Price, Game

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    price_value = serializers.CharField(source='price.price', read_only=True)

    class Meta:
        model = Game
        fields = '__all__'