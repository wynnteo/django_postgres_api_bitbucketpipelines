from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from django.http import HttpResponse

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def welcome_view(request):
    return HttpResponse("Hello World")