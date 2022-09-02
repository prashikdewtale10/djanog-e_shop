from django.shortcuts import render, redirect
from store.models import  Customer
from django.contrib.auth.hashers import make_password
from django.views import View  #to create class based views

class Signup(View):
    def get(self,request):
         return render(request, 'signup.html')
    
    def post(self,request):
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
    # print(fname,lname,phone,email,password)
    # validation of data
        data_values = {
                'firstname': fname,
                'lastname': lname,
                'phone': phone,
                'email': email,
        }
        customer = Customer(first_name=fname, last_name=lname,
                            phone=phone, email=email, password=password)
        err_msg=self.ValidateCustomer(customer)
        if not err_msg:
            # saving  data
            print("Error message", err_msg)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("index")
        else:
            data = {
                'err': err_msg,
                'values': data_values
        }
            return render(request, "signup.html", data)
    
    def ValidateCustomer(self,customer):
        err_msg = None
        if (not customer.first_name):
            err_msg = "First name required"
        elif len(customer.first_name) < 4:
            err_msg = "First name must be 4 more character long"
        elif (not customer.last_name):
            err_msg = "Last name required"
        elif len(customer.last_name) < 4:
            err_msg = "Last name must be 4 more character long"
        elif (not customer.phone):
            err_msg = "Phone no required"
        elif len(customer.phone) < 10:
            err_msg = "Phone no must be 10 char long"
        elif len(customer.password) < 6:
            err_msg = "Password must be 8 char long"
        elif len(customer.email) < 5:
            err_msg = "Email must be 5 char long"
        elif customer.isEmailExist():
            err_msg = "Account is already registed with this email"
        return err_msg
