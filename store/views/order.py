from itertools import product
from django.views import View
from django.shortcuts import render ,redirect
from store.models import Customer, Product , Order
from store.middleware.auth import auth_middleware
# from django.utils.decorators import method_decorator

class OrdersView(View):
    # @method_decorator(auth_middleware)
    def get(self,request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer_id(customer)
        print(orders)
        return render(request,'orders.html',{'orders':orders})