from django.urls import path
from .views import *

urlpatterns = [
   path('productlist/', productlist, name='productlist'),
   path('addproduct', addproduct, name='addproduct'),
   path('updateproduct/<int:product_id>', updateproduct, name='updateproduct'),
   path('deleteproduct/<int:product_id>', deleteproduct, name='deleteproduct')
]