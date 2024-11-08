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

]
