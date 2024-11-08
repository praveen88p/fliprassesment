from rest_framework import serializers
from .models import Product, CartItem, Order
from django.contrib.auth import authenticate
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])  
        user.save()
        return user


class SigninSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")
        
        user = authenticate(username=user.username, password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")
        
        data['user'] = user
        return data
    

class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        extra_kwargs = {field: {'required': False} for field in fields}  

from rest_framework import serializers
from .models import CartItem, Product

class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid product ID.")
        return value


class UpdateCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=0)

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid product ID.")
        return value

    def validate(self, data):
        product_id = data['product_id']
        quantity = data['quantity']

        if quantity > 0:
            product = Product.objects.get(id=product_id)
            if quantity > product.stock: 
                raise serializers.ValidationError("Requested quantity exceeds available stock.")
        return data
    

class PlaceOrderSerializer(serializers.Serializer):
    shipping_address = serializers.CharField(max_length=500)    


class OrderPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 100    
