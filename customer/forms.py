from django import forms 
from django.forms import ModelForm
from .models import Customer_Profile,Book_Table
from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm
from restaurant import settings
from django.db import transaction
from django.contrib.admin import widgets


User=get_user_model()




GENDER_CHOICES = (
	('Select', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    



# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ('name','email','subject','message','mobile')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


CATEGORY_CHOICES = (
    ('Select', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )



class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=15, required=True)
    last_name = forms.CharField(max_length=15, required=True)
    mobile_number = forms.CharField(max_length=10, required=True)
    email = forms.EmailField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = (

            'username',
            'email',
            'password1',
            'password2'
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        cp = Customer_Profile.objects.create(user=user)

        cp.image = self.cleaned_data.get('image')
        cp.gender = self.cleaned_data.get('gender')
        cp.dateofbirth = self.cleaned_data.get('dateofbirth')
        cp.present_location = self.cleaned_data.get('present_location')
        cp.permanent_address = self.cleaned_data.get('permanent_address')
        cp.local_address = self.cleaned_data.get('local_address')
        cp.mobile = self.cleaned_data.get('mobile')
        cp.save()
        return user



class DateInput(forms.DateInput):
    input_type = 'date'

class BooktableForm(forms.ModelForm):
    place      = forms.CharField()
    book_time  = forms.TimeField(widget=widgets.AdminTimeWidget)

    class Meta():
        model = Book_Table
        fields = ['place','customer','book_date','book_time']
        widgets = {
            'book_date': DateInput(attrs={'type': 'date'})
        }




























        





