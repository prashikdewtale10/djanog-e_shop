from django.urls import path , include
from store.views import indexview , login, order,signup , cart , checkout , order
from store.middleware.auth import auth_middleware
urlpatterns = [
    path('',indexview.Index.as_view(),name="index"),
    path('signup',signup.Signup.as_view(),name="signup"),
    path('login',login.Login.as_view(),name="login"),
    path('logout',login.Logout,name="logout"),
    path('cart',cart.Cart.as_view(),name="cart"),
    path('check-out',checkout.CheckOut.as_view(),name="check-out"),
    path('orders',auth_middleware(order.OrdersView.as_view()),name="orders"),


    
]
