from django.forms import ModelForm
from product.models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        # fields = ['product_name']
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"