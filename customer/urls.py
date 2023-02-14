from django.urls import path
from .import views
app_name = 'customer'
urlpatterns = [

   path("",views.cust_home,name='home'),
   path("updateprofile",views.cust_update,name='updateprofile'),
   path("orderhistory",views.order_history,name='orderhistory'),
   path("changepassword",views.change_password,name='changepassword'),
   path("productdetails/<int:pid>",views.product_det,name='productdetails'),
   path("viewcart",views.view_cart,name='viewcart'),
   path("cust_home_page",views.cust_home_page,name='cust_home_page'),
   path("logout",views.logout,name='logout'),
   path("cart/<int:pid>",views.add_cart,name='add_to_cart'),

   path("find_total",views.total_price,name='total'),
   path("remove_item/<int:pid>",views.remove_item,name='remove_item'),
   path("order_product",views.order_product,name='order_product'),
]