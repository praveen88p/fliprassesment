from decimal import Decimal
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from .models import Product, CartItem, Order, OrderItem
from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer
from django.contrib.auth.models import User
from .serializers import SignupSerializer, AddToCartSerializer, UpdateProductSerializer, UpdateCartSerializer, SigninSerializer, PlaceOrderSerializer,OrderSerializer, OrderPagination
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser 

# Product Management

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.save()
        success_message = {
            "message": "Product added successfully",
            "product_id": product.id,
            "stock": product.stock  
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
        user = serializer.save()  
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

#function for the signin
@api_view(['POST'])
def signin(request):
    serializer = SigninSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        tokens = get_tokens_for_user(user)  # Generate JWT tokens
        return Response(
            {
                "message": "Login successful",
                "tokens": tokens
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# function for update the products
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



#function for deleting product
@api_view(['DELETE'])
def delete_product(request, productId):
    try:
        product = Product.objects.get(id=productId)  
    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found."},
            status=status.HTTP_404_NOT_FOUND
        )

    product.delete()
    return Response(
        {"message": "Product deleted successfully"},
        status=status.HTTP_200_OK
    )



#function for Add product to cart
@api_view(['POST'])
@permission_classes([IsAuthenticated])  
def add_to_cart(request):
    serializer = AddToCartSerializer(data=request.data)
    if serializer.is_valid():
        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data['quantity']
        
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,  
            product_id=product_id,
            defaults={'quantity': quantity}
        )
        
        if not created:
            
            new_quantity = cart_item.quantity + quantity
            if new_quantity > product.stock:
                return Response(
                    {"error": "Requested quantity exceeds available stock."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            cart_item.quantity = new_quantity
            cart_item.save()
        else:
           
            if quantity > product.stock:
                return Response(
                    {"error": "Requested quantity exceeds available stock."},
                    status=status.HTTP_400_BAD_REQUEST
                )

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



@api_view(['PUT'])
@permission_classes([IsAuthenticated]) 
def update_cart(request):
    serializer = UpdateCartSerializer(data=request.data)
    if serializer.is_valid():
        product_id = serializer.validated_data['product_id']
        new_quantity = serializer.validated_data['quantity']
        
        try:
            cart_item = CartItem.objects.get(user=request.user, product_id=product_id)
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Product not found in cart."},
                status=status.HTTP_404_NOT_FOUND
            )

        if new_quantity == 0:
            cart_item.delete()
            return Response(
                {"message": "Product removed from cart."},
                status=status.HTTP_200_OK
            )

        product = Product.objects.get(id=product_id)
        if new_quantity > product.stock:
            return Response(
                {"error": "Requested quantity exceeds available stock."},
                status=status.HTTP_400_BAD_REQUEST
            )

        cart_item.quantity = new_quantity
        cart_item.save()

        return Response(
            {
                "message": "Cart updated successfully.",
                "cart_item": {
                    "product_id": cart_item.product.id,
                    "quantity": cart_item.quantity
                }
            },
            status=status.HTTP_200_OK
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  
def delete_cart_item(request):
    product_id = request.data.get('product_id')
    
    if not product_id:
        return Response(
            {"error": "Product ID is required."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        cart_item = CartItem.objects.get(user=request.user, product_id=product_id)
    except CartItem.DoesNotExist:
        return Response(
            {"error": "Product not found in cart."},
            status=status.HTTP_404_NOT_FOUND
        )
    
    cart_item.delete()

    remaining_items = CartItem.objects.filter(user=request.user)
    cart_details = [
        {
            "product_id": item.product.id,
            "quantity": item.quantity
        }
        for item in remaining_items
    ]

    return Response(
        {
            "message": "Product removed from cart successfully.",
            "updated_cart": cart_details
        },
        status=status.HTTP_200_OK
    )



@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def get_cart_details(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    if not cart_items.exists():
        return Response(
            {"message": "Your cart is empty."},
            status=status.HTTP_200_OK
        )
    
    total_amount = 0
    cart_details = []
    for item in cart_items:
        product = item.product
        item_total = product.price * item.quantity  
        total_amount += item_total 
        cart_details.append({
            "product_id": product.id,
            "name": product.name,
            "description": product.description,
            "quantity": item.quantity,
            "price_per_unit": product.price,
            "total_price": item_total
        })

    return Response(
        {
            "message": "Cart retrieved successfully.",
            "cart_items": cart_details,
            "total_amount": total_amount
        },
        status=status.HTTP_200_OK
    )




@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def place_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        return Response(
            {"error": "Your cart is empty."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    serializer = PlaceOrderSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    total_amount = Decimal(0.0)
    for item in cart_items:
        total_amount += item.product.price * item.quantity

    order = Order.objects.create(
        user=request.user,
        shipping_address=serializer.validated_data['shipping_address'],
        total_amount=total_amount
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price  
        )
        item.product.stock -= item.quantity
        item.product.save()
    
    cart_items.delete()

    return Response(
        {
            "message": "Order placed successfully.",
            "order_id": order.order_id,
            "total_amount": total_amount,
            "shipping_address": order.shipping_address
        },
        status=status.HTTP_201_CREATED
    )






@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def get_all_orders(request):
    
    orders_query = Order.objects.all()

    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    if start_date and end_date:
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            orders_query = orders_query.filter(created_at__range=[start_date, end_date])
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)
    
    order_status = request.query_params.get('status', None)
    if order_status:
        orders_query = orders_query.filter(status=order_status)

    paginator = OrderPagination()
    paginated_orders = paginator.paginate_queryset(orders_query, request)

    order_serializer = OrderSerializer(paginated_orders, many=True)

    return paginator.get_paginated_response(order_serializer.data)

@api_view(['GET'])
 
def get_orders_by_customer(request, customerId):
    try:
        customer = User.objects.get(id=customerId) 
    except User.DoesNotExist:
        return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)


    orders = Order.objects.filter(user=customer)  

    paginator = OrderPagination()
    paginated_orders = paginator.paginate_queryset(orders, request)

    serializer = OrderSerializer(paginated_orders, many=True)

    return paginator.get_paginated_response(serializer.data)
