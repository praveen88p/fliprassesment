from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Product, CartItem, Order
from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer
from django.contrib.auth.models import User
from .serializers import SignupSerializer, AddToCartSerializer, UpdateProductSerializer
from .serializers import SigninSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

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
    
    
    error_message = {
        "message": "Product creation failed",
        "errors": serializer.errors
    }
    return Response(error_message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # Save the user
        return Response(
            {"message": "User registered successfully", "user_id": user.id},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
def signin(request):
    serializer = SigninSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        tokens = get_tokens_for_user(user)  
        return Response(
            {
                "message": "Login successful",
                "tokens": tokens
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_product(request, productId):
    try:
        product = Product.objects.get(id=productId)  
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    
    serializer = UpdateProductSerializer(product, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()  
        return Response(
            {"message": "Product updated successfully"},
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def delete_product(request, productId):
    try:
        product = Product.objects.get(id=productId) 
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    # Delete the product
    product.delete()
    return Response(
        {"message": "Product deleted successfully"},
        status=status.HTTP_200_OK
    )




@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def add_to_cart(request):
    serializer = AddToCartSerializer(data=request.data)
    if serializer.is_valid():
        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']
        
       
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,  
            product_id=product_id,
            defaults={'quantity': quantity}
        )
        
        if not created:
           
            cart_item.quantity += quantity
            cart_item.save()

        return Response(
            {
                "message": "Product added to cart successfully.",
                "cart_item": {
                    "product_id": cart_item.product.id,
                    "quantity": cart_item.quantity
                }
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
