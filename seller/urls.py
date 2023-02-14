from django.urls import path
from .import views
app_name = 'seller'
urlpatterns = [

   path("",views.seller_home,name='sellerhome'),
   path("productcatelog",views.product_catelog,name='productcatelog'),
   path("updatestock",views.update_stock,name='updatestock'),
   path("changepassword",views.change_password,name='changepassword'),
   path("viewprofile",views.profile,name='viewprofile'),
   path("addproduct",views.add_product,name='addproduct'),
   path("logout",views.logout,name='logout'),

]