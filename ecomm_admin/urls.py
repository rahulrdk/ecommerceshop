from django.urls import path
from .import views
app_name = 'ecomm_admin'
urlpatterns = [
   path("",views.homepage,name='home'),
   path("viewseller",views.view_seller,name='viewseller'),
   path("approveseller",views.approve_seller,name='approveseller'),
   path("viewcustomer",views.view_customer,name='viewcustomer'),
   path("load_seller",views.load_seller,name='load_seller'),
   path("load_all_seller",views.load_all_seller,name='load_all_seller'),
   path("load_customer",views.load_customer,name='load_customer'),
   path("del_seller",views.del_seller,name='del_seller'),
   path("approvels",views.approvels,name='approvels'),
   path("logout",views.logout,name='logout'),

]