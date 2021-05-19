from django.urls import path
from . import views 
from .views import * 

urlpatterns = [

    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('contact/', ContactView.as_view(), name = 'contact'),
    path('csr/', views.csr, name = 'csr'),
    path('gallary/', views.gallaryView.as_view(), name = 'gallary'),
    path('life/', views.life, name = 'life'),
]

