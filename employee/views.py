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
from .forms import EmployeeSignUpForm
from .models import User , Employee_Profile
from employee.utils import account_activation_token
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .forms import ProfileForm
User=get_user_model()




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
    return render(request,'emaiverify.html')




class Employee_Register(CreateView):
    model = Employee_Profile
    form_class = EmployeeSignUpForm
    template_name = 'employee/emp_register.html'

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

        link = reverse('activate', kwargs={
                                'uidb64': email_body['uid'], 'token': email_body['token']})
        email_subject = 'Activate your account'
        activate_url = 'http://' + current_site.domain + link
        email = EmailMessage(
            email_subject,
            'Hi ' + user.username + ', Please the link below to activate your account \n' + activate_url,
             'noreply@semycolon.com',[email],)
        email.send(fail_silently=False)
        return redirect('emaiverify')

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login'+'?message='+'User already activated')

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as ex:
            pass

        return redirect('login')

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')



            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html', context={'form': AuthenticationForm()})



def Logout(request):
    logout(request)
    return redirect('register')


def Dashboard(request):
    return render(request,"dashboard.html")


def E_Profile(request):
    print("----user",request.user)
    emp_ = Employee_Profile.objects.filter(user=request.user)
    print("---ggggg------",emp_)
    return render (request,  'employee/emp_profile.html',{"emp_profile":emp_})