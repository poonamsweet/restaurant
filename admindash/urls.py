from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from.views import EmailValidationView,VerificationView,Admin_Register,emaiverify,AdminLogin,Logout,Home,AdminDashboard







urlpatterns = [

    path('', Home, name="home"),
    # path('register/', register, name='register'),
    path('adminregister/', Admin_Register.as_view(), name='adminregister'),
    path('admindashboard/', AdminDashboard, name='admindashboard'),
    path('adminemailverify/', emaiverify, name="adminemailverify"),
    path('validate_email', csrf_exempt(EmailValidationView.as_view()), name='validate_email'),
    path('adminactivate/<uidb64>/<token>', VerificationView.as_view(), name='adminactivate'),
    path('adminlogin/', AdminLogin, name='adminlogin'),
    path('adminlogout/', Logout, name='adminlogout'),

]
