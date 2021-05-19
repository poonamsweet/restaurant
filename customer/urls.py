from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from.views import EmailValidationView,VerificationView
from . views import  Customer_Register,Home,register,CustomerLogin,emaiverify,Logout,Dashboard,BookTable,CustomerProfile






urlpatterns = [

    path('', Home,name="home"),
    path('register/', register, name='register'),
    path('customerregister/', Customer_Register.as_view(), name='customerregister'),
    path('customeremailverify/', emaiverify, name="customeremailverify"),
    path('validate_email', csrf_exempt(EmailValidationView.as_view()), name='validate_email'),
    path('customeractivate/<uidb64>/<token>', VerificationView.as_view(), name='customeractivate'),
    path('customerlogin/', CustomerLogin, name='customerlogin'),
    path('customerlogout/', Logout, name='customerlogout'),
    path('customerdashboard/', Dashboard, name='customerdashboard'),
    path('customerprofile/', CustomerProfile, name='customerprofile'),
    path('book', BookTable, name='book'),
    
    path('table', Home,name="table"),

]
