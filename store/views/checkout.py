from itertools import product
from django.views import View
from django.shortcuts import render ,redirect
from store.models import Customer, Product , Order
class CheckOut(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_ids(list(cart.keys()))
        for product in products:
            order = Order(customer = Customer(customer),
                            product=product,
                            price=product.price,
                            address=address,
                            mobile=phone,
                            quantity=cart.get(str(product.id)))
            order.placeOrder()
            request.session['cart']={}
        print(address,phone,customer,cart,products)
        return redirect('cart')