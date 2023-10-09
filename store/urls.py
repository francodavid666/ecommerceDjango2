from django.urls import path
from .import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('',views.store, name = 'store'),
    path ('cart/',views.cart, name = 'cart'),
    path ('view_product/<id>/',views.view_product, name = 'view_product'),
    path ('checkout/',views.checkout, name = 'checkout'),
    path('update_item/', views.updateItem, name= 'update_item'),
    path('process_order/', views.processOrder, name= 'process_order'),
    path('userRegisterForm/', views.userRegisterForm, name= 'userRegisterForm'),
    path('userLoginForm/', views.userLoginForm, name= 'userLoginForm'),
    path('logout/', LogoutView.as_view(), name='logout'),
   
]