from django.shortcuts import render, redirect ,HttpResponseRedirect
from store.models import  Customer
from django.contrib.auth.hashers import  check_password
from django.views import View  #to create class based views

# LOGIN CLASS BASED VIEWS
class Login(View):
    returnUrl = None
    def get(self,request):
        Login.returnUrl=request.GET.get('return_Url')
        print("============================",Login.returnUrl)
        return render(request,'login.html')

    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        customer = Customer.get_custome_by_email(email)
        print(customer.email,customer.password)
        err_msg=None
        if customer:
            flag = check_password(password,customer.password)
            print(flag)
            if flag:
                request.session['customer']=customer.id
                # request.session['email']=customer.email
                if Login.returnUrl:
                    return HttpResponseRedirect(Login.returnUrl)
                else:
                    Login.returnUrl=None
                    return redirect("index")
            else:
                err_msg="Email or Password is invalid !!"
        else:
            err_msg="Email or Password is invalid !!"
        return render(request,'login.html',{'err':err_msg})

def Logout(request):
    request.session.clear()
    return redirect('login')