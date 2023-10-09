from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import JsonResponse
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from . utils import cookieCart, cartData, guestOrder

# Create your views here.

def userRegisterForm(request):
    if request.method == 'POST':
        form =  CustomerForm(request.POST)
        
        
        if form.is_valid():
            # Crear un nuevo Customer
            customer = form.save(commit=False)
           
             # Obtener datos del formulario relacionados con el usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            # Crear un usuario y establecer la relación con el cliente
            customer.create_user(username, password,email)            

           #messages.success (request,'¡Usuario creado creado!')
            print(form.cleaned_data)
            return redirect('store')
        else:
            print(form.errors)
            return redirect('userRegisterForm')
    else:
        
        form =  CustomerForm()
        context = {'form':form}
        return render (request,'store/userRegisterForm.html',context)


  


#LOGIN
def userLoginForm(request):
    if request.method =='POST':
        form=UserLoginForm(request,data=request.POST)
        if form.is_valid():
           
            username = request.POST["username"]
            password =request.POST["password"]

            usuario = authenticate(username = username, password = password)
            if usuario is not None:
                login(request,usuario)
                return redirect('store')
            else:
                print(form.cleaned_data)
                return redirect('userLoginForm')

        else:
            print(form.errors)
            form = UserLoginForm()
            context = {'form':form}
            return render (request,'store/userLoginForm.html',context)
    else:
        form = UserLoginForm()
        context = {'form':form}
        return render (request,'store/userLoginForm.html',context)




def store (request):

    cookieData = cartData(request)
    cartItems = cookieData['cartItems']

    products = Product.objects.all() 
    context = {'products': products, 'cartItems': cartItems,'shipping':False}
    return render (request,'store/store.html',context)

def view_product (request,id):
    cookieData = cartData(request)
    cartItems = cookieData['cartItems']

    products = Product.objects.filter(id = id) 
    context = {'products': products, 'cartItems': cartItems,'shipping':False}

    return  render (request, 'store/view.html',context)

def cart (request):
    cookieData = cartData(request)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']

    context = {'items':items, 'order':order,'cartItems': cartItems,'shipping':False}
    return render (request,'store/cart.html',context)



def checkout (request):
 
    cookieData = cartData(request)
    cartItems = cookieData['cartItems']
    order = cookieData['order']
    items = cookieData['items']
    context = {'items':items, 'order':order,'cartItems': cartItems,'shipping':False}
    return render (request,'store/checkout.html',context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action )
    print('ProductId:', productId )
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)       

    orderItem ,created = OrderItem.objects.get_or_create(order=order, product= product) 

    if action  == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe = False)


@csrf_exempt
def processOrder(request):
    #print ('Data', request.body)
    transaction_id  = datetime.datetime.now().timestamp() 
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)       
       

     
    else:
        customer, order=guestOrder(request,data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode'],
            )

    return JsonResponse('Payment complete', safe = False)


