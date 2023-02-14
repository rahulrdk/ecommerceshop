from urllib.request import Request
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from .models import *
from common.models import Customer
from seller.models import Product
from .decorator import auth_customer
import datetime

# Create your views here.
@auth_customer
def cust_home(request):
    return render(request,'customer/customer_home.html')


@auth_customer
def cust_update(request):
    return render(request,'customer/update_profile.html')

@auth_customer
def cust_home_page(request):
    return render(request,'customer/cust_home_page.html')

@auth_customer
def order_history(request):
    items = Order.objects.filter(customer=request.session['cust_id'])
    return render(request,'customer/order_history.html',{'items':items})


@auth_customer
def change_password(request):
    return render(request,'customer/change_password.html')



@auth_customer
def product_det(request,pid):
    if 'cust_id' in request.session:
        product = Product.objects.get(id=pid)
    else:
        return redirect('common:customerlogin')
    return render(request,'customer/product_details.html',{'product':product})


@auth_customer
def view_cart(request):
    cart_items = Cart.objects.filter(customer=request.session['cust_id'])

    return render(request,'customer/view_cart.html',{'cart_items':cart_items})

@auth_customer
def add_cart(request,pid):
    msg =''
    
    if 'cust_id' in request.session:
        product = Product.objects.get(id=pid)
        customer = Customer.objects.get(id =  request.session['cust_id'])
        product_exist = Cart.objects.filter(customer =request.session['cust_id'], product=pid).exists()
        if not product_exist:
            cart = Cart(customer = customer,product = product)
            cart.save()
            if request.session['cart_msg']:
                
                del request.session['cart_msg']
            return redirect('common:home')

        else:
            
            request.session['cart_msg'] = 'already in cart'
            
            
            return redirect('common:home')
    else:
        return redirect('common:customerlogin')


   

def logout(request):
    del request.session['cust_id']
    request.session.flush()
    return redirect('common:home')

@auth_customer
def total_price(request):
    
    
    qty = request.POST['qty']
    price = request.POST['price']
    total = int(qty) * float(price)
    print(total)
    return JsonResponse({'total':total})

@auth_customer
def remove_item(request,pid):
    product = Product.objects.get(id=pid)
    customer = Customer.objects.get(id =  request.session['cust_id'])
    item =Cart.objects.get(customer =request.session['cust_id'], product=pid)
    item.delete()
    return redirect('customer:viewcart')


def order_product(request):
    customer = request.session['cust_id']
    product = request.POST['product']
    order_date = datetime.datetime.now().time()
    delivery_status = 'order placed'
    address = request.POST['address']
    payment_id = request.POST['payment_id']

    payment_type = 'online'
    payment_amount = request.POST['amount']
    orders = Order(customer_id = customer,product_id = product,order_date = order_date,delivery_status= delivery_status,address = address,payment_id = payment_id,payment_type = payment_type,payment_amount = payment_amount)
    orders.save()
