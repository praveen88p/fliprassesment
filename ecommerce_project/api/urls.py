from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products, name='list_products'),
    path('addproduct', views.add_product, name='add_product'),
  path('signup/', views.signup, name='signup'),
  path('signin/', views.signin, name='signin'),
  path('updateproduct/<int:productId>/', views.update_product, name='update_product'),
      path('deleteproduct/<int:productId>/', views.delete_product, name='delete_product'),
        path('cart/add', views.add_to_cart, name='add_to_cart'),
    path('cart/update', views.update_cart, name='update_cart'),

    path('cart/delete', views.delete_cart_item, name='delete_cart_item'),
    path('cart', views.get_cart_details, name='get_cart_details'),
    path('placeorder', views.place_order, name='place_order'),
    path('getallorders', views.get_all_orders, name='get_all_orders'),
    path('orders/customer/<int:customerId>', views.get_orders_by_customer, name='get_orders_by_customer'),





]
