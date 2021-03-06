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
from .forms import AdminSignUpForm
from .models import User , Admin_Profile
from customer.models import User,Customer_Profile
from employee.models import Employee_Profile
from customer.utils import account_activation_token
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError

User=get_user_model()

def Home(request):
    return render(request, "index.html")


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'sorry email in use,choose another one '}, status=409)
        return JsonResponse({'email_valid': True})




def emaiverify(request):
    return render(request,'admin/emaiverify.html')




class Admin_Register(CreateView):
    model = Admin_Profile
    form_class = AdminSignUpForm
    template_name = 'admin/admin_register.html'

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

        link = reverse('adminactivate', kwargs={
                                'uidb64': email_body['uid'], 'token': email_body['token']})
        email_subject = 'Activate your account'
        activate_url = 'http://' + current_site.domain + link
        email = EmailMessage(
            email_subject,
            'Hi ' + user.username + ', Please the link below to activate your account \n' + activate_url,
             'noreply@semycolon.com',[email],)
        print(email)
        email.send(fail_silently=False)
        return redirect('adminemailverify')


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('adminlogin'+'?message='+'User already activated')

            if user.is_active:
                return redirect('adminlogin')
            user.is_active = True
            user.save()
            messages.success(request, 'Account activated successfully')
            return redirect('adminlogin')

        except Exception as ex:
            pass

        return redirect('adminlogin')

def AdminLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admindashboard')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'admin/adminlogin.html', context={'form': AuthenticationForm()})



def Logout(request):
    logout(request)
    # return render(request,"teacher/logout.html")
    return redirect('register')

def AdminDashboard(request):
    customer= Customer_Profile.objects.all()
    employee = Employee_Profile.objects.all()
    print("customer ",customer)
    print("employee ", employee)
    return render(request,"admin/adminhome.html",{"customer":customer,"employee":employee})





