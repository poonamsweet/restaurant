from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from.views import EmailValidationView,VerificationView
from . views import  Customer_Register,Home,register,CustomerLogin,emaiverify,Logout,Dashboard,Book_Table,CustomerProfile






urlpatterns = [

    path('', Home,name="home"),
    path('register/', register, name='register'),
    path('customerregister/', Customer_Register.as_view(), name='customerregister'),
    path('emailverify/', emaiverify, name="emaiverify"),
    path('validate_email', csrf_exempt(EmailValidationView.as_view()), name='validate_email'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('customerlogin/', CustomerLogin, name='customerlogin'),
    path('logout/', Logout, name='logout'),
    path('customerdashboard/', Dashboard, name='customerdashboard'),
    path('customerprofile/', CustomerProfile, name='customerprofile'),
    path('book/', Book_Table, name='book'),
]
