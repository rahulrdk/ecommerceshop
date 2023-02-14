from urllib.request import Request
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from common.views import seller_signup
from .decorator import auth_admin
from django.conf import settings
from django.core.mail import send_mail


import seller
from .models import *
from common.models import Seller
from common.models import Customer
# Create your views here.

@auth_admin
def homepage(request):
    return render(request,'ecomm_admin/ecomm_home.html')

@auth_admin
def view_seller(request):
    return render(request,'ecomm_admin/view_seller.html')

@auth_admin
def approve_seller(request):

    return render(request,'ecomm_admin/approve_seller.html')

@auth_admin
def view_customer(request):
    return render(request,'ecomm_admin/view_customer.html')

@auth_admin
def load_seller(request):
    approve_sellers = Seller.objects.filter(seller_status = 'pending')

    data = [{'id': seller.id, 'name': seller.seller_name, 'address': seller.seller_adds,
              'email': seller.seller_email,'phone': seller.seller_phone,'image': seller.seller_image.url
              } for seller in approve_sellers]
    print(data)
   

    return JsonResponse({'data': data})

@auth_admin
def load_all_seller(request):
    approved_seller = Seller.objects.filter(seller_status = 'approved')
    data = [{'id':seller.id,'name':seller.seller_name, 'address':seller.seller_adds, 'email':seller.seller_email, 'phone':seller.seller_phone,'image':seller.seller_image.url } for seller in approved_seller] 
    return JsonResponse({'data' : data})

@auth_admin
def load_customer(request):
    customers = Customer.objects.all()
    data = [{'id':customer.id,'name':customer.cust_name,'email':customer.cust_email,'phone':customer.cust_phone,'image':customer.cust_image.url} for customer in customers]
    return JsonResponse({'data':data})

@auth_admin
def del_seller(request):
    id = request.POST['id']
    sellers = Seller.objects.get(id=id)
    sellers.delete()
    return JsonResponse({'status': 'seller Deleted Succesfully'})

@auth_admin
def approvels(request):
    id = request.POST['id']
    sellers = Seller.objects.get(id=id)
    sellers.seller_status='approved'
    sellers.save()
    subject = 'approved'
    sellername = sellers.seller_name
    message = 'Hi {sellername},we are pleased to inform you that  ypur request has been approved'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [sellers.seller_email]
    send_mail(subject,message,email_from,recipient_list)
    return JsonResponse({'status': 'seller approved Succesfully'})

def logout(request):
    del request.session['admin_id']
    request.session.flush()
    return redirect('common:home')

