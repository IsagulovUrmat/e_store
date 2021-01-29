from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def products_page(request):
    products = Products.objects.all() #SELECT * FROM PRODUCTS
    return render(request,'products/products.html',{"products":products})

def order_page(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request,'products/order.html',{"form":form})

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'products/signup.html', {'form': form})

def user_page(request):
    user = User.objects.all()
    return render(request, 'products/user.html', {"user": user})

def about_us(request):
    aboutus = AboutUs.objects.all()
    return render(request, 'products/aboutus.html', {"aboutus": aboutus})

def contacts_page(request):
    contact = Contacts.objects.all()
    return render(request, 'products/contacts.html', {"contact": contact})



