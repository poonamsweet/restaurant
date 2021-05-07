from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import SESignUpForm, ABMSignUpForm, RBMSignUpForm, ZBMSignUpForm 
from django.contrib.auth.forms import AuthenticationForm
from .models import User , Salesexecutive
from validate_email import validate_email
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from accounts.utils import account_activation_token
from django.contrib import messages
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.views import View
from django.urls import reverse
from accounts .models import Salesexecutive,Abm,Rbm,Zbm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic import View
from django.utils import timezone
from .render import Render
from django.contrib import auth

















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
    return render(request, '../templates/accounts/register.html')

def emaiverify(request):
    return render(request,'../templates/accounts/emaiverify.html')


def SignUpForm(request):
    if request.method=="POST":
        if  request.POST['pass1'] == request.POST['pass2']:
        # both  the password matched
        # if previous user exists
           try:
                user =User.objects.get(username=request.POST.get('username'))
                return render(request,"../templates/accounts/employee_register.html",{"error":"User has already taken"})
           except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['pass1'],email=request.POST['email'])
                mobile_number = request.POST['mobile_number']
                
                birthdate = request.POST['birthdate']
                gender = request.POST['gender']
                height = request.POST['height']
                weight = request.POST['weight']
                identification_mark = request.POST['identification_mark']
                blood_group = request.POST['blood_group']
                maritual_status = request.POST['select_status']
                marriage_date = request.POST['marriage_date']
                Nationality = request.POST['Nationality']
                address_line_1 = request.POST['address_line_1']
                address_line_2 = request.POST['address_line_2']
                pin = request.POST['pin']
                city = request.POST['city']
                state = request.POST['state']
                mailing_address = request.POST['mailing_address']
                mail_address_line_1 = request.POST['mail_address_line_1']
                mail_address_line_2 = request.POST['mail_address_line_2']
                mail_pin = request.POST['mail_pin']
                mail_city = request.POST['mail_city']
                mail_state = request.POST['mail_state']
                bank_name = request.POST['bank_name']
                account_no = request.POST['account_no']
                pan_no = request.POST['pan_no']
                pan_pic =request.FILES['pan_pic']
                passport_no = request.POST['passport_no']
                passport_pic    = request.FILES['passport_pic']
                driving_license = request.POST['driving_license']
                dl_pic = request.FILES['dl_pic']
                high_school = request.POST['high_school']
                high_school_passing_year = request.POST['high_school_passing_year']
                high_school_marks_obtained = request.POST['high_school_marks_obtained']
                high_school_cert = request.FILES['high_school_cert']
                intermediate_school = request.POST['intermediate_school']
                intermediate_passing_year = request.POST['intermediate_passing_year']
                intermediate_marks_obtained = request.POST['intermediate_marks_obtained']
                intermediate_cert = request.FILES['intermediate_cert']
                Degree_obtained = request.POST['Degree_obtained']
                college_institute = request.POST['college_institute']
                Year_of_passing = request.POST['Year_of_passing']
                marks_obtained = request.POST['marks_obtained']
                degree_cert = request.FILES['degree_cert']
                experience = request.POST['experience']
                organisation_name = request.POST['organisation_name']
                position_held = request.POST['position_held']
                hq = request.POST['hq']
                date_of_joining = request.POST['date_of_joining']
                date_of_leaving = request.POST['date_of_leaving']
                father_name = request.POST['father_name']
                mother_name = request.POST['mother_name']
                brother = request.POST['brother']
                sister = request.POST['sister']
                spouces_name = request.POST['spouces_name']
                children_count = request.POST['children_count']
              
                
                extended_user = Profile(mobile_number=mobile_number,birthdate=birthdate,gender=gender,
                height=height,weight=weight,identification_mark=identification_mark,blood_group=blood_group,maritual_status=maritual_status,
                marriage_date=marriage_date,Nationality=Nationality,address_line_1=address_line_1,address_line_2=address_line_2,
                pin=pin,city=city,state=state,mailing_address=mailing_address,mail_address_line_1=mail_address_line_1,mail_address_line_2=mail_address_line_2,
                mail_pin=mail_pin,mail_city=mail_city,mail_state=mail_state,bank_name=bank_name,account_no=account_no,pan_no=pan_no,pan_pic=pan_pic,
                passport_no=passport_no,passport_pic=passport_pic,driving_license=driving_license,dl_pic=dl_pic,high_school=high_school,
                high_school_passing_year=high_school_passing_year,high_school_marks_obtained=high_school_marks_obtained,high_school_cert=high_school_cert,
                intermediate_school=intermediate_school,intermediate_passing_year=intermediate_passing_year,intermediate_marks_obtained=intermediate_marks_obtained,
                intermediate_cert=intermediate_cert,Degree_obtained=Degree_obtained,college_institute=college_institute,Year_of_passing=Year_of_passing,
                marks_obtained=marks_obtained,degree_cert=degree_cert,experience=experience,organisation_name=organisation_name,
                position_held=position_held,hq=hq,date_of_joining=date_of_joining,date_of_leaving=date_of_leaving,father_name=father_name,
                mother_name=mother_name,brother=brother,sister=sister,spouces_name=spouces_name,children_count=children_count,user=user)
                extended_user.save()
                user.is_se = True
                user.save()
                sales_user=Salesexecutive(profile=extended_user,user=user)
                sales_user.save()
                return render(request,"../templates/accounts/login.html",{"message":"Signned Up Successfully!"})
                


              
        else:
            return render(request, "../templates/accounts/employee_register.html", {"error": "Password Don't Match"})
    else:
        return render(request, "../templates/accounts/employee_register.html")


class se_register(CreateView):
    model = User
    form_class = SESignUpForm
    template_name = '../templates/accounts/se_register.html'

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
        print(email)
        email.send(fail_silently=False)
        return redirect('emaiverify')

        

class abm_register(CreateView):
    model = User
    form_class = ABMSignUpForm
    template_name = '../templates/accounts/abm_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
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
        print(email)
        email.send(fail_silently=False)
        return redirect('emaiverify')


class rbm_register(CreateView):
    model = User
    form_class = RBMSignUpForm
    template_name = '../templates/accounts/rbm_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
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
            email_subject,'Hi ' + user.username + ', Please the link below to activate your account \n' + activate_url,
                                'noreply@semycolon.com',[email],)
        print(email)
        email.send(fail_silently=False)
        return redirect('emaiverify')


class zbm_register(CreateView):
    model = User
    form_class = ZBMSignUpForm
    template_name = '../templates/accounts/zbm_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
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
        print(email)
        email.send(fail_silently=False)
        return redirect('emaiverify')



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/accounts/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')





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




class Se_Pdf(View):

    def get(self, request):
        sales = Salesexecutive.objects.filter(user=request.user)
        today = timezone.now()
        params = {
            'today': today,
            'sales': sales,
            'request': request
        }
        return Render.render('../templates/accounts/se_pdf.html', params)


def se_profile(request):
    Sales_executive = Salesexecutive.objects.filter(user=request.user)
    return render (request,  '../templates/accounts/se_profile.html',{"se_profile":Sales_executive})


class ABm_Pdf(View):

    def get(self, request):
        abm_pdf = Abm.objects.filter(user = request.user)
        today = timezone.now()
        params = {
            'today': today,
            'abm_pdf': abm_pdf,
            'request': request
        }
        return Render.render('../templates/accounts/abm_pdf.html', params)

def abm_profile(request):
    abm_executive = Abm.objects.filter(user = request.user)
    return render (request,  '../templates/accounts/abm_profile.html',{"abm_executive":abm_executive})


class RBM_Pdf(View):

    def get(self, request):
        rbm_pdf = Rbm.objects.filter(user = request.user)
        today = timezone.now()
        params = {
            'today': today,
            'rbm_pdf': rbm_pdf,
            'request': request
        }
        return Render.render('../templates/accounts/rbm_pdf.html', params)

def rbm_profile(request):
    rbm_executive = Rbm.objects.filter(user = request.user)
    return render (request,  '../templates/accounts/rbm_profile.html',{"rbm_executive":rbm_executive})


class ZBM_Pdf(View):

    def get(self, request):
        zbm_pdf = Zbm.objects.filter(user = request.user)
        today = timezone.now()
        params = {
            'today': today,
            'zbm_pdf': zbm_pdf,
            'request': request
        }
        return Render.render('../templates/accounts/zbm_pdf.html', params)

def zbm_profile(request):
    zbm_executive = Zbm.objects.filter(user = request.user)
    return render (request,  '../templates/accounts/zbm_profile.html',{"zbm_executive":zbm_executive})




