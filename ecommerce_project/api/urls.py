# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products, name='list_products'),
    path('addproduct', views.add_product, name='add_product'),
    # other routes for sign up, sign in, cart management, etc.
]
