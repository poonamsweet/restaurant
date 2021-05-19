from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.forms import ModelForm
from django.db import transaction
from .models import User,Salesexecutive , Abm , Zbm , Rbm
from company import settings


CATEGORY_CHOICES = (
    ('Select', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
CATEGORY_MARRIED_CHOICES = (
    ('Select', 'Select'),
        ('Married', 'Married'),
        ('Single', 'Single'),
    )
    
EXPERIENCE_CHOICES = (
    ('Select', 'Select'),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    
MAILING_CHOICES = (
    ('Select', 'Select'),
        ('Same', 'Same'),
        ('Different', 'Different'),
    )






class SESignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 15 , required=True)
    last_name = forms.CharField(max_length = 15 , required=True)
    mobile_number = forms.CharField(max_length = 10 ,required=True)
    email = forms.EmailField(required=True)
    location = forms.CharField( max_length = 50, required=True)
    birthdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)


    gender = forms.ChoiceField(choices = CATEGORY_CHOICES)
    height = forms.CharField( max_length = 8)
    weight = forms.CharField(max_length = 7)
    identification_mark = forms.CharField(max_length = 50)
    blood_group = forms.CharField(max_length = 3)
    
    maritual_status = forms.ChoiceField(choices = CATEGORY_MARRIED_CHOICES)
    marriage_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
    Nationality = forms.CharField(max_length = 6)
    
#permanent adress

    address_line_1= forms.CharField(max_length = 30)
    address_line_2= forms.CharField(max_length = 30)
    pin= forms.CharField(max_length = 56)
    city= forms.CharField( max_length = 15)
    state= forms.CharField( max_length = 30)
    
    
    #mailing address

    mailing_address= forms.ChoiceField(choices=MAILING_CHOICES)
    mail_address_line_1= forms.CharField(max_length = 30)
    mail_address_line_2= forms.CharField(max_length = 30)
    mail_pin= forms.CharField( max_length = 6)
    mail_city= forms.CharField(max_length = 15)
    mail_state= forms.CharField(max_length = 30)
    

    bank_name        = forms.CharField(max_length = 20)
    account_no       =forms.CharField(max_length = 20)
    pan_no           =forms.CharField(max_length = 20)
    pan_pic           =forms.ImageField()
    passport_no      =forms.CharField(max_length = 20) 
    passport_pic      =forms.FileField() 
    driving_license   =forms.CharField(max_length = 20)
    driving_license_pic   =forms.FileField()

    #Educational details

    high_school=forms.CharField(max_length = 30)
    high_school_passing_year=forms.CharField(max_length = 4)
    high_school_marks_obtained=forms.CharField(max_length = 5)
    high_school_cert=forms.FileField()

    intermediate_school=forms.CharField(max_length = 30)
    intermediate_passing_year=forms.CharField(max_length = 4)
    intermediate_marks_obtained=forms.CharField(max_length = 5)
    intermediate_cert=forms.FileField()

    Degree_obtained=forms.CharField(max_length = 30)
    college_institute =forms.CharField(max_length = 50)
    Year_of_passing=forms.CharField(max_length = 4)
    marks_obtained    =forms.CharField(max_length = 5)
    degree_cert       = forms.FileField()
    
    #Professional details

    experience        = forms.ChoiceField(choices=EXPERIENCE_CHOICES)
    organisation_name =forms.CharField(max_length = 50)
    position_held     =forms.CharField(max_length = 20)
    head_quater                =forms.CharField(max_length = 50)
    date_of_joining   =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
    date_of_leaving   =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
      
        #family details

    father_name       =forms.CharField(max_length = 20)
    mother_name       =forms.CharField(max_length = 20)
    brother           =forms.CharField(max_length = 1)
    sister            =forms.CharField(max_length = 1)
    spouse_name       =forms.CharField(max_length = 20)
    children_count=forms.CharField(max_length = 1)



    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_se = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.mobile_number=self.cleaned_data.get('mobile_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        se = Salesexecutive.objects.create(user=user)
        
        se.location = self.cleaned_data.get('location')
        se.birthdate = self.cleaned_data.get('birthdate')
        se.birthdate_cert = self.cleaned_data.get('birthdate_cert')
        se.gender = self.cleaned_data.get('gender')
        se.height = self.cleaned_data.get('height')
        se.weight = self.cleaned_data.get('weight')
        se.identification_mark = self.cleaned_data.get('identification_mark')
        se.blood_group = self.cleaned_data.get('blood_group')
        se.maritual_status = self.cleaned_data.get('maritual_status')
        se.marriage_date = self.cleaned_data.get('marriage_date')
        se.Nationality = self.cleaned_data.get('Nationality')


        se.address_line_1 = self.cleaned_data.get('address_line_1')
        se.address_line_2 = self.cleaned_data.get('address_line_2')
        se.pin = self.cleaned_data.get('pin')
        se.city = self.cleaned_data.get('city')
        se.state = self.cleaned_data.get('state')
        se.mailing_address = self.cleaned_data.get('mailing_address')
        se.mail_address_line_1 = self.cleaned_data.get('mail_address_line_1')
        se.mail_address_line_2 = self.cleaned_data.get('mail_address_line_2')
        se.mail_pin = self.cleaned_data.get('mail_pin')
        se.mail_city = self.cleaned_data.get('mail_city')
        se.mail_state = self.cleaned_data.get('mail_state')
     

        se.bank_name = self.cleaned_data.get('bank_name')
        se.account_no = self.cleaned_data.get('account_no')
        se.pan_no = self.cleaned_data.get('pan_no')
        se.pan_pic = self.cleaned_data.get('pan_pic')

        se.passport_no = self.cleaned_data.get('passport_no')
        se.passport_pic=self.cleaned_data.get('passport_pic')
        se.driving_license = self.cleaned_data.get('driving_license')
        se.driving_license_pic = self.cleaned_data.get('driving_license_pic')
        se.high_school = self.cleaned_data.get('high_school')

        se.high_school_passing_year = self.cleaned_data.get('high_school_passing_year')
        se.high_school_marks_obtained = self.cleaned_data.get('high_school_marks_obtained')
        se.high_school_cert = self.cleaned_data.get('high_school_cert')
        se.intermediate_school = self.cleaned_data.get('intermediate_school')

        se.intermediate_passing_year = self.cleaned_data.get('intermediate_passing_year')
        se.intermediate_marks_obtained = self.cleaned_data.get('intermediate_marks_obtained')
        se.intermediate_cert = self.cleaned_data.get('intermediate_cert')
        se.Degree_obtained = self.cleaned_data.get('Degree_obtained')

        se.college_institute = self.cleaned_data.get('college_institute')
        se.Year_of_passing = self.cleaned_data.get('Year_of_passing')
        se.marks_obtained = self.cleaned_data.get('marks_obtained')
        se.degree_cert = self.cleaned_data.get('degree_cert')
        se.experience = self.cleaned_data.get('experience')


        se.organisation_name = self.cleaned_data.get('organisation_name')
        se.position_held = self.cleaned_data.get('position_held')
        se.head_quater = self.cleaned_data.get('head_quater')
        se.date_of_joining = self.cleaned_data.get('date_of_joining')
        se.date_of_leaving = self.cleaned_data.get('date_of_leaving')

        se.father_name = self.cleaned_data.get('father_name')
        se.mother_name = self.cleaned_data.get('mother_name')
        se.brother = self.cleaned_data.get('brother')
        se.sister = self.cleaned_data.get('sister')
        se.spouse_name = self.cleaned_data.get('spouse_name')
        se.children_count = self.cleaned_data.get('children_count')
        se.save()
        return user

class ABMSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length = 15 , required=True)
    last_name = forms.CharField(max_length = 15 , required=True)
    mobile_number = forms.CharField(max_length = 10 ,required=True)
    email = forms.EmailField(required=True)
    area = forms.CharField( max_length = 50, required=True)
    birthdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)


    gender = forms.ChoiceField(choices = CATEGORY_CHOICES)
    height = forms.CharField( max_length = 8)
    weight = forms.CharField(max_length = 7)
    identification_mark = forms.CharField(max_length = 50)
    blood_group = forms.CharField(max_length = 3)
    
    maritual_status = forms.ChoiceField(choices = CATEGORY_MARRIED_CHOICES)
    marriage_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
    Nationality = forms.CharField(max_length = 6)
    
#permanent adress

    address_line_1= forms.CharField(max_length = 30)
    address_line_2= forms.CharField(max_length = 30)
    pin= forms.CharField(max_length = 56)
    city= forms.CharField( max_length = 15)
    state= forms.CharField( max_length = 30)
    
    
    #mailing address

    mailing_address= forms.ChoiceField(choices=MAILING_CHOICES)
    mail_address_line_1= forms.CharField(max_length = 30)
    mail_address_line_2= forms.CharField(max_length = 30)
    mail_pin= forms.CharField( max_length = 6)
    mail_city= forms.CharField(max_length = 15)
    mail_state= forms.CharField(max_length = 30)
    

    bank_name        = forms.CharField(max_length = 20)
    account_no       =forms.CharField(max_length = 20)
    pan_no           =forms.CharField(max_length = 20)
    pan_pic           =forms.ImageField()
    passport_no      =forms.CharField(max_length = 20) 
    passport_pic      =forms.FileField() 
    driving_license   =forms.CharField(max_length = 20)
    driving_license_pic   =forms.FileField()

    #Educational details

    high_school=forms.CharField(max_length = 30)
    high_school_passing_year=forms.CharField(max_length = 4)
    high_school_marks_obtained=forms.CharField(max_length = 5)
    high_school_cert=forms.FileField()

    intermediate_school=forms.CharField(max_length = 30)
    intermediate_passing_year=forms.CharField(max_length = 4)
    intermediate_marks_obtained=forms.CharField(max_length = 5)
    intermediate_cert=forms.FileField()

    Degree_obtained=forms.CharField(max_length = 30)
    college_institute =forms.CharField(max_length = 50)
    Year_of_passing=forms.CharField(max_length = 4)
    marks_obtained    =forms.CharField(max_length = 5)
    degree_cert       = forms.FileField()
    
    #Professional details

    experience        = forms.ChoiceField(choices=EXPERIENCE_CHOICES)
    organisation_name =forms.CharField(max_length = 50)
    position_held     =forms.CharField(max_length = 20)
    head_quater                =forms.CharField(max_length = 50)
    date_of_joining   =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
    date_of_leaving   =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
      
        #family details

    father_name       =forms.CharField(max_length = 20)
    mother_name       =forms.CharField(max_length = 20)
    brother           =forms.CharField(max_length = 1)
    sister            =forms.CharField(max_length = 1)
    spouse_name       =forms.CharField(max_length = 20)
    children_count=forms.CharField(max_length = 1)




    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_abm = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.mobile_number=self.cleaned_data.get('mobile_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        abm = Abm.objects.create(user=user)
        
        abm.area = self.cleaned_data.get('area')
        abm.birthdate = self.cleaned_data.get('birthdate')
        abm.birthdate_cert = self.cleaned_data.get('birthdate_cert')
        abm.gender = self.cleaned_data.get('gender')
        abm.height = self.cleaned_data.get('height')
        abm.weight = self.cleaned_data.get('weight')
        abm.identification_mark = self.cleaned_data.get('identification_mark')
        abm.blood_group = self.cleaned_data.get('blood_group')
        abm.maritual_status = self.cleaned_data.get('maritual_status')
        abm.marriage_date = self.cleaned_data.get('marriage_date')
        abm.Nationality = self.cleaned_data.get('Nationality')


        abm.address_line_1 = self.cleaned_data.get('address_line_1')
        abm.address_line_2 = self.cleaned_data.get('address_line_2')
        abm.pin = self.cleaned_data.get('pin')
        abm.city = self.cleaned_data.get('city')
        abm.state = self.cleaned_data.get('state')
        abm.mailing_address = self.cleaned_data.get('mailing_address')
        abm.mail_address_line_1 = self.cleaned_data.get('mail_address_line_1')
        abm.mail_address_line_2 = self.cleaned_data.get('mail_address_line_2')
        abm.mail_pin = self.cleaned_data.get('mail_pin')
        abm.mail_city = self.cleaned_data.get('mail_city')
        abm.mail_state = self.cleaned_data.get('mail_state')
     

        abm.bank_name = self.cleaned_data.get('bank_name')
        abm.account_no = self.cleaned_data.get('account_no')
        abm.pan_no = self.cleaned_data.get('pan_no')
        abm.pan_pic = self.cleaned_data.get('pan_pic')

        abm.passport_no = self.cleaned_data.get('passport_no')
        abm.passport_pic=self.cleaned_data.get('passport_pic')
        abm.driving_license = self.cleaned_data.get('driving_license')
        abm.driving_license_pic = self.cleaned_data.get('driving_license_pic')
        abm.high_school = self.cleaned_data.get('high_school')

        abm.high_school_passing_year = self.cleaned_data.get('high_school_passing_year')
        abm.high_school_marks_obtained = self.cleaned_data.get('high_school_marks_obtained')
        abm.high_school_cert = self.cleaned_data.get('high_school_cert')
        abm.intermediate_school = self.cleaned_data.get('intermediate_school')

        abm.intermediate_passing_year = self.cleaned_data.get('intermediate_passing_year')
        abm.intermediate_marks_obtained = self.cleaned_data.get('intermediate_marks_obtained')
        abm.intermediate_cert = self.cleaned_data.get('intermediate_cert')
        abm.Degree_obtained = self.cleaned_data.get('Degree_obtained')

        abm.college_institute = self.cleaned_data.get('college_institute')
        abm.Year_of_passing = self.cleaned_data.get('Year_of_passing')
        abm.marks_obtained = self.cleaned_data.get('marks_obtained')
        abm.degree_cert = self.cleaned_data.get('degree_cert')
        abm.experience = self.cleaned_data.get('experience')


        abm.organisation_name = self.cleaned_data.get('organisation_name')
        abm.position_held = self.cleaned_data.get('position_held')
        abm.head_quater = self.cleaned_data.get('head_quater')
        abm.date_of_joining = self.cleaned_data.get('date_of_joining')
        abm.date_of_leaving = self.cleaned_data.get('date_of_leaving')

        abm.father_name = self.cleaned_data.get('father_name')
        abm.mother_name = self.cleaned_data.get('mother_name')
        abm.brother = self.cleaned_data.get('brother')
        abm.sister = self.cleaned_data.get('sister')
        abm.spouse_name = self.cleaned_data.get('spouse_name')
        abm.children_count = self.cleaned_data.get('children_count')
        abm.save()
        return user

class ZBMSignUpForm(UserCreationForm):
   first_name = forms.CharField(max_length = 15 , required=True)
   last_name = forms.CharField(max_length = 15 , required=True)
   mobile_number = forms.CharField(max_length = 10 ,required=True)
   email = forms.EmailField(required=True)
   zone = forms.CharField( max_length = 50, required=True)
   birthdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
   gender = forms.ChoiceField(choices = CATEGORY_CHOICES)
   height = forms.CharField( max_length = 8)
   weight = forms.CharField(max_length = 7)
   identification_mark = forms.CharField(max_length = 50)
   blood_group = forms.CharField(max_length = 3)
   maritual_status = forms.ChoiceField(choices = CATEGORY_MARRIED_CHOICES)
   marriage_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
   Nationality = forms.CharField(max_length = 6)
    
#permanent adress
   address_line_1= forms.CharField(max_length = 30)
   address_line_2= forms.CharField(max_length = 30)
   pin= forms.CharField(max_length = 56)
   city= forms.CharField( max_length = 15)
   state= forms.CharField( max_length = 30)
    
    
    #mailing address

   mailing_address= forms.ChoiceField(choices=MAILING_CHOICES)
   mail_address_line_1= forms.CharField(max_length = 30)
   mail_address_line_2= forms.CharField(max_length = 30)
   mail_pin= forms.CharField( max_length = 6)
   mail_city= forms.CharField(max_length = 15)
   mail_state= forms.CharField(max_length = 30)
    

   bank_name        = forms.CharField(max_length = 20)
   account_no       =forms.CharField(max_length = 20)
   pan_no           =forms.CharField(max_length = 20)
   pan_pic           =forms.ImageField()
   passport_no      =forms.CharField(max_length = 20) 
   passport_pic      =forms.FileField() 
   driving_license   =forms.CharField(max_length = 20)
   driving_license_pic   =forms.FileField()

    #Educational details

   high_school=forms.CharField(max_length = 30)
   high_school_passing_year=forms.CharField(max_length = 4)
   high_school_marks_obtained=forms.CharField(max_length = 5)
   high_school_cert=forms.FileField()

   intermediate_school=forms.CharField(max_length = 30)
   intermediate_passing_year=forms.CharField(max_length = 4)
   intermediate_marks_obtained=forms.CharField(max_length = 5)
   intermediate_cert=forms.FileField()

   Degree_obtained=forms.CharField(max_length = 30)
   college_institute =forms.CharField(max_length = 50)
   Year_of_passing=forms.CharField(max_length = 4)
   marks_obtained    =forms.CharField(max_length = 5)
   degree_cert       = forms.FileField()
    
    #Professional details

   experience        = forms.ChoiceField(choices=EXPERIENCE_CHOICES)
   organisation_name =forms.CharField(max_length = 50)
   position_held     =forms.CharField(max_length = 20)
   head_quater                =forms.CharField(max_length = 50)
   date_of_joining   =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
   date_of_leaving   =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
      
        #family details

   father_name       =forms.CharField(max_length = 20)
   mother_name       =forms.CharField(max_length = 20)
   brother           =forms.CharField(max_length = 1)
   sister            =forms.CharField(max_length = 1)
   spouse_name       =forms.CharField(max_length = 20)
   children_count=forms.CharField(max_length = 1)



   class Meta(UserCreationForm.Meta):
        model = User

   @transaction.atomic
   def save(self):
        user = super().save(commit=False)
        user.is_zbm = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.mobile_number=self.cleaned_data.get('mobile_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        zbm = Zbm.objects.create(user=user)
        
        zbm.zone = self.cleaned_data.get('zone')
        zbm.birthdate = self.cleaned_data.get('birthdate')
        zbm.birthdate_cert = self.cleaned_data.get('birthdate_cert')
        zbm.gender = self.cleaned_data.get('gender')
        zbm.height = self.cleaned_data.get('height')
        zbm.weight = self.cleaned_data.get('weight')
        zbm.identification_mark = self.cleaned_data.get('identification_mark')
        zbm.blood_group = self.cleaned_data.get('blood_group')
        zbm.maritual_status = self.cleaned_data.get('maritual_status')
        zbm.marriage_date = self.cleaned_data.get('marriage_date')
        zbm.Nationality = self.cleaned_data.get('Nationality')


        zbm.address_line_1 = self.cleaned_data.get('address_line_1')
        zbm.address_line_2 = self.cleaned_data.get('address_line_2')
        zbm.pin = self.cleaned_data.get('pin')
        zbm.city = self.cleaned_data.get('city')
        zbm.state = self.cleaned_data.get('state')
        zbm.mailing_address = self.cleaned_data.get('mailing_address')
        zbm.mail_address_line_1 = self.cleaned_data.get('mail_address_line_1')
        zbm.mail_address_line_2 = self.cleaned_data.get('mail_address_line_2')
        zbm.mail_pin = self.cleaned_data.get('mail_pin')
        zbm.mail_city = self.cleaned_data.get('mail_city')
        zbm.mail_state = self.cleaned_data.get('mail_state')
     

        zbm.bank_name = self.cleaned_data.get('bank_name')
        zbm.account_no = self.cleaned_data.get('account_no')
        zbm.pan_no = self.cleaned_data.get('pan_no')
        zbm.pan_pic = self.cleaned_data.get('pan_pic')

        zbm.passport_no = self.cleaned_data.get('passport_no')
        zbm.passport_pic=self.cleaned_data.get('passport_pic')
        zbm.driving_license = self.cleaned_data.get('driving_license')
        zbm.driving_license_pic = self.cleaned_data.get('driving_license_pic')
        zbm.high_school = self.cleaned_data.get('high_school')

        zbm.high_school_passing_year = self.cleaned_data.get('high_school_passing_year')
        zbm.high_school_marks_obtained = self.cleaned_data.get('high_school_marks_obtained')
        zbm.high_school_cert = self.cleaned_data.get('high_school_cert')
        zbm.intermediate_school = self.cleaned_data.get('intermediate_school')

        zbm.intermediate_passing_year = self.cleaned_data.get('intermediate_passing_year')
        zbm.intermediate_marks_obtained = self.cleaned_data.get('intermediate_marks_obtained')
        zbm.intermediate_cert = self.cleaned_data.get('intermediate_cert')
        zbm.Degree_obtained = self.cleaned_data.get('Degree_obtained')

        zbm.college_institute = self.cleaned_data.get('college_institute')
        zbm.Year_of_passing = self.cleaned_data.get('Year_of_passing')
        zbm.marks_obtained = self.cleaned_data.get('marks_obtained')
        zbm.degree_cert = self.cleaned_data.get('degree_cert')
        zbm.experience = self.cleaned_data.get('experience')


        zbm.organisation_name = self.cleaned_data.get('organisation_name')
        zbm.position_held = self.cleaned_data.get('position_held')
        zbm.head_quater = self.cleaned_data.get('head_quater')
        zbm.date_of_joining = self.cleaned_data.get('date_of_joining')
        zbm.date_of_leaving = self.cleaned_data.get('date_of_leaving')

        zbm.father_name = self.cleaned_data.get('father_name')
        zbm.mother_name = self.cleaned_data.get('mother_name')
        zbm.brother = self.cleaned_data.get('brother')
        zbm.sister = self.cleaned_data.get('sister')
        zbm.spouse_name = self.cleaned_data.get('spouse_name')
        zbm.children_count = self.cleaned_data.get('children_count')
        zbm.save()
        return user

    


class RBMSignUpForm(UserCreationForm):
   first_name = forms.CharField(max_length = 15 , required=True)
   last_name = forms.CharField(max_length = 15 , required=True)
   mobile_number = forms.CharField(max_length = 10 ,required=True)
   email = forms.EmailField(required=True)
   region = forms.CharField( max_length = 50, required=True)
   birthdate = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)


   gender = forms.ChoiceField(choices = CATEGORY_CHOICES)
   height = forms.CharField( max_length = 8)
   weight = forms.CharField(max_length = 7)
   identification_mark = forms.CharField(max_length = 50)
   blood_group = forms.CharField(max_length = 3)
    
   maritual_status = forms.ChoiceField(choices = CATEGORY_MARRIED_CHOICES)
   marriage_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
   Nationality = forms.CharField(max_length = 6)
    
#permanent adress

   address_line_1= forms.CharField(max_length = 30)
   address_line_2= forms.CharField(max_length = 30)
   pin= forms.CharField(max_length = 56)
   city= forms.CharField( max_length = 15)
   state= forms.CharField( max_length = 30)
    
    
    #mailing address

   mailing_address= forms.ChoiceField(choices=MAILING_CHOICES)
   mail_address_line_1= forms.CharField(max_length = 30)
   mail_address_line_2= forms.CharField(max_length = 30)
   mail_pin= forms.CharField( max_length = 6)
   mail_city= forms.CharField(max_length = 15)
   mail_state= forms.CharField(max_length = 30)
    

   bank_name        = forms.CharField(max_length = 20)
   account_no       =forms.CharField(max_length = 20)
   pan_no           =forms.CharField(max_length = 20)
   pan_pic           =forms.ImageField()
   passport_no      =forms.CharField(max_length = 20) 
   passport_pic      =forms.FileField() 
   driving_license   =forms.CharField(max_length = 20)
   driving_license_pic   =forms.FileField()

    #Educational details

   high_school=forms.CharField(max_length = 30)
   high_school_passing_year=forms.CharField(max_length = 4)
   high_school_marks_obtained=forms.CharField(max_length = 5)
   high_school_cert=forms.FileField()

   intermediate_school=forms.CharField(max_length = 30)
   intermediate_passing_year=forms.CharField(max_length = 4)
   intermediate_marks_obtained=forms.CharField(max_length = 5)
   intermediate_cert=forms.FileField()

   Degree_obtained=forms.CharField(max_length = 30)
   college_institute =forms.CharField(max_length = 50)
   Year_of_passing=forms.CharField(max_length = 4)
   marks_obtained    =forms.CharField(max_length = 5)
   degree_cert       = forms.FileField()
    
    #Professional details

   experience        = forms.ChoiceField(choices=EXPERIENCE_CHOICES)
   organisation_name =forms.CharField(max_length = 50)
   position_held     =forms.CharField(max_length = 20)
   head_quater                =forms.CharField(max_length = 50)
   date_of_joining   =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS) 
   date_of_leaving   =forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
      
        #family details

   father_name       =forms.CharField(max_length = 20)
   mother_name       =forms.CharField(max_length = 20)
   brother           =forms.CharField(max_length = 1)
   sister            =forms.CharField(max_length = 1)
   spouse_name       =forms.CharField(max_length = 20)
   children_count=forms.CharField(max_length = 1)



   class Meta(UserCreationForm.Meta):
        model = User
    
   @transaction.atomic
   def save(self):
        user = super().save(commit=False)
        user.is_rbm = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.mobile_number=self.cleaned_data.get('mobile_number')
        user.email = self.cleaned_data.get('email')
        user.save()
        rbm = Rbm.objects.create(user=user)

        
        rbm.region = self.cleaned_data.get('region')
        rbm.birthdate = self.cleaned_data.get('birthdate')
        rbm.birthdate_cert = self.cleaned_data.get('birthdate_cert')
        rbm.gender = self.cleaned_data.get('gender')
        rbm.height = self.cleaned_data.get('height')
        rbm.weight = self.cleaned_data.get('weight')
        rbm.identification_mark = self.cleaned_data.get('identification_mark')
        rbm.blood_group = self.cleaned_data.get('blood_group')
        rbm.maritual_status = self.cleaned_data.get('maritual_status')
        rbm.marriage_date = self.cleaned_data.get('marriage_date')
        rbm.Nationality = self.cleaned_data.get('Nationality')


        rbm.address_line_1 = self.cleaned_data.get('address_line_1')
        rbm.address_line_2 = self.cleaned_data.get('address_line_2')
        rbm.pin = self.cleaned_data.get('pin')
        rbm.city = self.cleaned_data.get('city')
        rbm.state = self.cleaned_data.get('state')
        rbm.mailing_address = self.cleaned_data.get('mailing_address')
        rbm.mail_address_line_1 = self.cleaned_data.get('mail_address_line_1')
        rbm.mail_address_line_2 = self.cleaned_data.get('mail_address_line_2')
        rbm.mail_pin = self.cleaned_data.get('mail_pin')
        rbm.mail_city = self.cleaned_data.get('mail_city')
        rbm.mail_state = self.cleaned_data.get('mail_state')
     

        rbm.bank_name = self.cleaned_data.get('bank_name')
        rbm.account_no = self.cleaned_data.get('account_no')
        rbm.pan_no = self.cleaned_data.get('pan_no')
        rbm.pan_pic = self.cleaned_data.get('pan_pic')

        rbm.passport_no = self.cleaned_data.get('passport_no')
        rbm.passport_pic=self.cleaned_data.get('passport_pic')
        rbm.driving_license = self.cleaned_data.get('driving_license')
        rbm.driving_license_pic = self.cleaned_data.get('driving_license_pic')
        rbm.high_school = self.cleaned_data.get('high_school')

        rbm.high_school_passing_year = self.cleaned_data.get('high_school_passing_year')
        rbm.high_school_marks_obtained = self.cleaned_data.get('high_school_marks_obtained')
        rbm.high_school_cert = self.cleaned_data.get('high_school_cert')
        rbm.intermediate_school = self.cleaned_data.get('intermediate_school')

        rbm.intermediate_passing_year = self.cleaned_data.get('intermediate_passing_year')
        rbm.intermediate_marks_obtained = self.cleaned_data.get('intermediate_marks_obtained')
        rbm.intermediate_cert = self.cleaned_data.get('intermediate_cert')
        rbm.Degree_obtained = self.cleaned_data.get('Degree_obtained')

        rbm.college_institute = self.cleaned_data.get('college_institute')
        rbm.Year_of_passing = self.cleaned_data.get('Year_of_passing')
        rbm.marks_obtained = self.cleaned_data.get('marks_obtained')
        rbm.degree_cert = self.cleaned_data.get('degree_cert')
        rbm.experience = self.cleaned_data.get('experience')


        rbm.organisation_name = self.cleaned_data.get('organisation_name')
        rbm.position_held = self.cleaned_data.get('position_held')
        rbm.head_quater = self.cleaned_data.get('head_quater')
        rbm.date_of_joining = self.cleaned_data.get('date_of_joining')
        rbm.date_of_leaving = self.cleaned_data.get('date_of_leaving')

        rbm.father_name = self.cleaned_data.get('father_name')
        rbm.mother_name = self.cleaned_data.get('mother_name')
        rbm.brother = self.cleaned_data.get('brother')
        rbm.sister = self.cleaned_data.get('sister')
        rbm.spouse_name = self.cleaned_data.get('spouse_name')
        rbm.children_count = self.cleaned_data.get('children_count')
        rbm.save()
        return user
"""

class ProfileForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    mobile_number = forms.CharField(required=True)
    image = forms.ImageField()
    info = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = Profile

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.mobile_number=self.cleaned_data.get('mobile_number')
        user.email=self.cleaned_data.get('email')
        user.save()

        profile = Profile.objects.create(user=user)
        profile.image = self.cleaned_data.get('image')
        profile.info = self.cleaned_data.get('info')
        profile.save()
        return user

"""