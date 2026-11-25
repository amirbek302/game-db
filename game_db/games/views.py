from django.shortcuts import render
from rest_framework import generics

from .models import Game, Category, Price
from .serializers import GameSerializer, CategorySerializer, PriceSerializer


# Create your views here.

# ------------------- ListCreateAPIView -----------------------
class GamesListAPIView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PriceListAPIView(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
# ------------------- ListCreateAPIView -----------------------


# ---------------- Detail ----------------------
class GameDetailAPIView(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
# ---------------- Detail ----------------------


# ------------------- Delete -----------------------
class GameDeleteAPIView(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class CategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PriceDeleteAPIView(generics.DestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

# ------------------- Delete -----------------------

# generics.RetrieveAPIView
# generics.DestroyAPIView

