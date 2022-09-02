
from django.shortcuts import render, redirect
from store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View  #to create class based views
from django.views import View
# Create your views here.

class Index(View):
    def get(self,request):
        # products = Product.get_all_products()
        _category = Category.get_all_category()
        # TO GET REQUETED DATA FROM UR
        print("You are",request.session.get('email'))
        print("You are",request.session.get('customer_id'))
        category__ID = request.GET.get('category_id', False)
        if category__ID:
            products = Product.get_all_products_by_Id(category__ID)
        else:
            products = Product.get_all_products()

        return render(request, 'index.html', {'products': products, 'category': _category})

    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product]= quantity +1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        
        request.session['cart']=cart
        print('YOUR CART:',request.session.get('cart'))
        return redirect("index")







        