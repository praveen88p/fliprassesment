# api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, CartItem, Order
from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer
from django.contrib.auth.models import User

# Product Management

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.save()
        success_message = {
            "message": "Product added successfully",
            "product_id": product.id
        }
        return Response(success_message, status=status.HTTP_201_CREATED)
    
    # Return custom error response if data is invalid
    error_message = {
        "message": "Product creation failed",
        "errors": serializer.errors
    }
    return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

# Example view to list all products
@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
