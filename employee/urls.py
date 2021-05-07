from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from.views import EmailValidationView,VerificationView
from . views import  Employee_Register,register,Login,emaiverify,Logout,Dashboard,E_Profile






urlpatterns = [
    path('register/', register, name='register'),
    path('employeeregister/', Employee_Register.as_view(), name='employeeregister'),
    path('emailverify/', emaiverify, name="emaiverify"),
    path('validate_email', csrf_exempt(EmailValidationView.as_view()), name='validate_email'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('employeeprofile/', E_Profile, name='employeeprofile'),
]
