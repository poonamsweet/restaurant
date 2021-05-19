from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from validate_email import validate_email
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.views.generic import CreateView

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from .forms import CustomerSignUpForm,BooktableForm,UnknownBooktableForm
from .models import User , Customer_Profile,Book_Table
from customer.utils import account_activation_token
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError

User=get_user_model()

def Home(request):
      if request.method=="POST":
        form = UnknownBooktableForm(request.POST)
        print("-----",form)
        if form.is_valid():
            form.save()
            print("form",form)
            return redirect('home')

  
      
      form= UnknownBooktableForm()
      return render(request, "index.html",{"form":form})




class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid': True})

def register(request):
        return render(request, 'register.html')


def emaiverify(request):
    return render(request,'customer/emaiverify.html')




class Customer_Register(CreateView):
    model = Customer_Profile
    form_class = CustomerSignUpForm
    template_name = 'customer/se_register.html'

    def form_valid(self,form):
        user = form.save()
        email = form.data.get('email')
        current_site = get_current_site(self.request)
        email_body = {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            }

        link = reverse('customeractivate', kwargs={
                                'uidb64': email_body['uid'], 'token': email_body['token']})
        email_subject = 'Activate your account'
        activate_url = 'http://' + current_site.domain + link
        email = EmailMessage(
            email_subject,
            'Hi ' + user.username + ', Please the link below to activate your account \n' + activate_url,
             'noreply@semycolon.com',[email],)
        print(email)
        email.send(fail_silently=False)
        return redirect('customeremailverify')

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('customerlogin'+'?message='+'User already activated')

            if user.is_active:
                return redirect('customerlogin')
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('customerlogin')

        except Exception as ex:
            pass

        return redirect('customerlogin')

def CustomerLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_customer == True:
                    print("------cutomer---")
                    return redirect('customerdashboard')



            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'customer/customerlogin.html', context={'form': AuthenticationForm()})

def CustomerProfile(request):
    print("----user",request.user)
    customer_ = Customer_Profile.objects.filter(user=request.user)

    return render (request,  'customer/se_profile.html',{"customer":customer_})



def Logout(request):
    logout(request)
    # return render(request,"teacher/logout.html")
    return redirect('register')

def Dashboard(request):
    return render(request,"customer/customerdashboard.html")



def BookTable(request):
    if request.method=="POST":
        bookuser = Customer_Profile.objects.get(user=request.user.id)
        print("---bookuser----",bookuser)

        form = BooktableForm(request.POST,instance=bookuser)

        if form.is_valid():
            user = form.save(commit=False)
            book_date= form.cleaned_data['book_date']
            book_time = form.cleaned_data['book_time']
            place   = form.cleaned_data['place']
            value = Book_Table(customervalue=bookuser,book_date=book_date,book_time=book_time,place=place)
            value.save()
            return redirect('customerdashboard')

    else:      
       form= BooktableForm()
       return render(request, "customer/booktable.html",{"form":form})





  

