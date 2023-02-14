from django.urls import path
from .import views
app_name = 'common'
urlpatterns = [

   path("",views.homepage,name='home'),
   path("customerlogin",views.customer_login,name='customerlogin'),
   path("sellerlogin",views.seller_login,name='sellerlogin'),
   path("adminlogin",views.admin_login,name='adminlogin'),
   path("customersignup",views.customer_signup,name='customersignup'),
   path("sellersignup",views.seller_signup,name='sellersignup'),
   path("seller_email_validate",views.seller_email_validate,name='seller_email_validate'),
   path("customer_email_validate",views.customer_email_validate,name='customer_email_validate'),
]