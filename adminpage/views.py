from django.shortcuts import render, redirect
from product.models import *
from .forms import ProductForm, CategoryForm

# Create your views here.
def productlist(request):
    product = Product.objects.all()
    data = {
        'product':product
    }
    return render(request, 'admins/productlist.html', data)

def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admins/addproduct')  # we have to declare url path in redirect
        else:
            return render(request, 'admins/addprodut.html', {'form':form})
    context = {
        'form':ProductForm
    }

    return render(request, 'admins/addproduct.html', context)
