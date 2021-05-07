from django.urls import path
from . import  views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from .views import EmailValidationView, VerificationView, Se_Pdf , ABm_Pdf , RBM_Pdf , ZBM_Pdf





urlpatterns=[
     path('register/',views.register, name='register'),
     path('sepdf/', Se_Pdf.as_view(),name="sepdf"),
     path('abmpdf/', ABm_Pdf.as_view(),name="abmpdf"),
     path('rbmpdf/', RBM_Pdf.as_view(),name="rbmpdf"),
     path('zbmpdf/', ZBM_Pdf.as_view(),name="zbmpdf"),
     #path('employee_register/',views.SignUpForm, name='employee_register'),
     path('se_register/',views.se_register.as_view(), name='se_register'),
     path('abm_register/',views.abm_register.as_view(), name='abm_register'),
     path('rbm_register/',views.rbm_register.as_view(), name='rbm_register'),
     path('zbm_register/',views.zbm_register.as_view(), name='zbm_register'),
     path('emailverify/',views.emaiverify, name='emaiverify'),
     path('validate_email', csrf_exempt(EmailValidationView.as_view()),name='validate_email'),
     path('activate/<uidb64>/<token>',VerificationView.as_view(), name='activate'),

     path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
     path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
     path('reset_done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('se_profile/',views.se_profile, name='se_profile'),
     path('abm_profile/',views.abm_profile, name='abm_profile'),
     path('rbm_profile/',views.rbm_profile, name='rbm_profile'),
     path('zbm_profile/',views.zbm_profile, name='zbm_profile'),
 ]
