from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from .models import * 
from django.urls import reverse_lazy 
# Create your views here.

def home (request):
	return render(request, 'info/index.html')

def about (request):
	return render(request, 'info/about.html')

def csr (request):
	return render(request, 'info/csr.html')


def life (request):
	return render(request, 'info/life.html')

class gallaryView (ListView):
	model = Gallary
	template = 'info/gallary_list.html'
	

class ContactView(CreateView):
	model = Contact
	fields = ['first_name', 'second_name' ,  'email' , 'mobile' , 'message' ] #describe the field need to create 
	success_url = reverse_lazy('home')



	

#def faq (request):
#	return render(request, 'info/faq.html')
