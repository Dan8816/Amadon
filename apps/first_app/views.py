from django.shortcuts import render, HttpResponse, redirect
from apps.first_app.models import Product
from django.contrib import messages
from time import localtime, strftime
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    context = {
        "products": Product.objects.all()        
    }
    return render(request, "first_app/index.html", context)

def buy(request):
    product_id = int(request.POST['product_id'])
    quantity = int(request.POST['quantity'])
    item_bought = Product.objects.get(id=product_id)
    item_bought.item_count += quantity
    item_bought.save()
    current_purchase = item_bought.price
    total_spent = 0
    total_items = 0

    for i in Product.objects.all():
        total_spent += (i.price * i.item_count)
        total_items = total_items + i.item_count

    request.session['current_purchase'] = float(current_purchase)
    request.session['total_spent'] = float(total_spent)
    request.session['total_items'] = total_items
    
    return redirect('/checkout')

def checkout(request):
    context = {
        'current_purchase' : request.session['current_purchase'],
        'total_spent' : request.session['total_spent'],
        'total_items' : request.session['total_items']
    }
    return render(request, "first_app/checkout.html", context)

