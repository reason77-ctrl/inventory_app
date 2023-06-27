from django.shortcuts import render,redirect
from .models import *
from .forms import AddStocksForm, SignUpForm
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse
from django.http import HttpResponseRedirect


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    items_by_category = {}
    for category in categories:
        items_by_category[category]=Product.objects.filter(category=category)

    context = {
        'products':products,
        'categories':categories,
        'items_by_category':items_by_category,

    }
    return render(request, 'index.html',context)


def categories(request, category_id, category_title):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    items_by_category = {}
    for category in categories:
        items_by_category[category]=Product.objects.filter(category=category)
    context={
        'category':category,
        'products':products,
        'items_by_category':items_by_category,
    }
    return render(request, 'index.html',context)


def add_category(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            fa_image = request.POST['fa_image']
            data = Category.objects.create(
                title = title,
                fa_image = fa_image,
            )
            data.save()
    return redirect('home:index')



def add_qty(request):
    if request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        quantity = Product.objects.get(id=product_id).quantity
        price = Product.objects.get(id=product_id).price
        added_qty = int(request.POST.get('added_qty'))
        if request.method == 'POST':
            if 'increment' in request.POST:
                total_qty = quantity + added_qty
                total_price = total_qty * price
                
            elif 'decrement' in request.POST:
                total_qty = quantity-added_qty
                total_price = total_qty * price
            Product.objects.filter(id=product_id).update(quantity=total_qty, total_price=total_price)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return redirect('home:index')




def add_stocks(request):
    form = AddStocksForm()
    if request.method == "POST":
        form = AddStocksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:add_stocks')

    return render(request, 'add_stocks.html',{'form':form})


def update_stocks(request, product_id):
    items = Product.objects.get(pk=product_id)
    form = AddStocksForm(request.POST or None,request.FILES or None, instance=items)
    if form.is_valid():
        form.save()
        return redirect('home:index')

    context = {
        'items':items,
        'form':form,
    }
    return render(request, 'update_stocks.html',context)


def delete_stock(request, product_id):
    items = Product.objects.get(pk=product_id)
    items.delete()
    return redirect('home:index')



def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']

            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('home:index')
    return render(request, "authenticate/signup.html",{'form':form})



def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            return redirect('home:login')
    else:
        return render(request, 'authenticate/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('home:index')