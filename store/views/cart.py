from django.views import View
from django.shortcuts import render
from store.models import Product
from django.http import HttpResponse
class Cart(View):
    def get(self,request):
        if not request.session.get('cart'):
            print("your cart is empty")
            return HttpResponse('<b>Your cart is empty</b>')
        else:
            ids = list(request.session.get('cart').keys())
            product = Product.get_products_by_ids(ids)
            print(product)
            return render(request,'cart.html' ,{'products':product})