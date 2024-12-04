from django.shortcuts import render, redirect
from product.models import *
from .forms import ProductForm, CategoryForm
from django.contrib import messages

# Create your views here.
# read function
def productlist(request):
    product = Product.objects.all()
    data = {
        'product':product
    }
    return render(request, 'admins/productlist.html', data)


#create function
def addproduct(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product updated successfully !')
            return redirect('/admins/addproduct')  # we have to declare url path in redirect
        else:
            messages.add_message(request, messages.ERROR, "Update failed !")
            return render(request, 'admins/addproduct.html', {'form':form})

    # this code is for display our ProductForm        
    context = {
        'form':ProductForm
    }

    return render(request, 'admins/addproduct.html', context)

#update function
def updateproduct(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product updated successfully !')
            return redirect('/admins/productlist')
        else:
            messages.add_message(request, messages.ERROR, "Update failed !")
            return render(request, 'admins/updateproduct.html', {'form':form})


    context = {
        'form':ProductForm(instance=product)
    }

    return render(request, 'admins/updateproduct.html', context)

#deletefunction
def deleteproduct(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request, messages.SUCCESS, 'Product deleted successfully !')
    return redirect('/admins/productlist')
      
