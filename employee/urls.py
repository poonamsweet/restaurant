from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from.views import EmailValidationView,VerificationView
from . views import  Employee_Register,register,EmployyLogin,emaiverify,Logout,Dashboard,E_Profile,EntryExit






urlpatterns = [
    # path('register/', register, name='register'),
    path('employeeregister/', Employee_Register.as_view(), name='employeeregister'),
    path('employeeemailverify/', emaiverify, name="employeeemailverify"),
    path('validate_email', csrf_exempt(EmailValidationView.as_view()), name='validate_email'),
    path('employeeactivate/<uidb64>/<token>', VerificationView.as_view(), name='employeeactivate'),
    path('employeelogin/', EmployyLogin, name='employeelogin'),
    path('employeelogout/', Logout, name='employeelogout'),
    path('employeedashboard/', Dashboard, name='employeedashboard'),
    path('employeeprofile/', E_Profile, name='employeeprofile'),
    path('entryexit/', EntryExit, name='entryexit'),
]
