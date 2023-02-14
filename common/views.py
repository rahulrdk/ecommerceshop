import json
from urllib.request import Request
from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from .models import *
from seller.models import Product
# Create your views here.
def homepage(request):
    msg=""
    if 'cart_msg' in request.session:
        msg = request.session['cart_msg']
    print(msg)
    products = Product.objects.all()
    return render(request,'common/project_home.html',{'products':products,'cart_msg':msg})


def customer_login(request):
    msg = ''
    if request.method ==  'POST':

        c_name = request.POST['cust_name']
        c_password = request.POST['cust_password']
        data_exists = Customer.objects.filter(cust_email = c_name,cust_password = c_password)
        if data_exists:
            cust_data = Customer.objects.get(cust_email = c_name,cust_password = c_password)
            request.session['cust_id'] = cust_data.id
            request.session['cust_name'] = cust_data.cust_name
            return redirect('common:home')
        else:
            msg = 'incorrect username or password'

    return render(request,'common/customer_login.html',{'message':msg})


def admin_login(request):
    msg = ''
    if request.method == 'POST':
        ad_id = request.POST['admin_id']
        ad_password = request.POST['admin_password']
        data_exists = Admin.objects.filter(admin_id = ad_id,admin_password = ad_password)
        if data_exists:
            admin_data = Admin.objects.get(admin_id = ad_id,admin_password = ad_password)
            request.session['admin_id'] = admin_data.id
            return redirect('ecomm_admin:home')
        else:
            msg = 'incorrect admin id or password'
    return render(request,'common/admin_login.html',{'message':msg})


def seller_login(request):
    msg=''
    if request.method == 'POST':
        s_name = request.POST['seller_name']
        s_pass = request.POST['seller_password']
        data_exits=Seller.objects.filter(seller_email=s_name,seller_password=s_pass).exists()
        if data_exits:
            seller_data=Seller.objects.get(seller_email=s_name,seller_password=s_pass)
            if seller_data.seller_status =='approved':
                 request.session['seller_id']=seller_data.id
                 return redirect('seller:sellerhome')
            else:
                msg = 'admin not approved!!! kindly wait'

           
        else:
            msg='incorrect username or password'

    return render(request,'common/seller_login.html',{'message':msg})




def customer_signup(request):
    msg=''
    if request.method == 'POST':
        c_name = request.POST['cust_name']
        c_eml = request.POST['cust_email']
        c_phone = request.POST['cust_phone']
        c_img = request.FILES['cust_file']
        c_passw = request.POST['cust_password']
       
        customer_exists=Customer.objects.filter(cust_email=c_eml).exists()
        if not customer_exists:

             obj = Customer(cust_name=c_name,cust_email=c_eml,cust_phone=c_phone,cust_image=c_img,cust_password=c_passw)
             obj.save()
             msg='success'
        
        else:
            msg='email already exist'

    return render(request,'common/customer_signup.html',{'message':msg})
    


def seller_signup(request):
     msg=''
     if request.method == 'POST':
        s_name = request.POST['seller_name']
        s_eml = request.POST['seller_email']
        s_phone = request.POST['seller_phone']
        s_img = request.FILES['seller_image']
        s_passw = request.POST['seller_password']
        s_adds = request.POST['seller_adds']
        s_accno = request.POST['seller_accno']
        s_ifsc = request.POST['seller_ifsc']
       
        seller_exists=Seller.objects.filter(seller_email=s_eml).exists()
        if not seller_exists:

             obj = Seller(seller_name=s_name,seller_email=s_eml,seller_phone=s_phone,seller_image=s_img,seller_password=s_passw,seller_adds=s_adds,seller_accno=s_accno,seller_ifsc=s_ifsc)
             obj.save()
             return redirect('common:home')
        
        else:
            msg='email already exist'

     return render(request,'common/seller_signup.html',{'message':msg})


def seller_email_validate(request):
    check_email = request.POST['email']
    seller_exists=Seller.objects.filter(seller_email = check_email).exists()
    
    return JsonResponse({'seller_exists':seller_exists})

def customer_email_validate(request):
    check_email = request.POST['email']
    customer_exists=Customer.objects.filter(cust_email = check_email).exists()
    
    return JsonResponse({'customer_exists':customer_exists})


    
