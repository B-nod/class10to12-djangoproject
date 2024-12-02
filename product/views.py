from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

# Create your views here.
# def home(request):
#     return HttpResponse("Welcome to Product Page")

def home(request):
    product = Product.objects.all()  #model
    data = {
        'p':product
    }
    return render(request, 'product/homepage.html', data)  #template

def product(request):
    product = Product.objects.all()  #model
    data = {
        'p':product
    }
    return render(request, 'product/productpage.html', data)  #template

def contact(request):
    return render(request, 'product/contacus.html')