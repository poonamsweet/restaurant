from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model

# Create your models here.


class User(AbstractUser):
    is_customer = models.BooleanField(default = False)
    is_employee = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length = 15,unique=True)
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    email = models.EmailField()


GENDER_CHOICES = (
    ('Select', 'Select'),
    ('Male', 'Male'),
    ('Female', 'Female'),

)

class Customer_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    gender = models.CharField(max_length=32, choices=GENDER_CHOICES, default="select",null=True,blank=True)
    dateofbirth = models.DateField(null=True,blank=True)
    present_location = models.CharField(max_length=30,null=True,blank=True)
    permanent_address = models.CharField(max_length=50,null=True,blank=True)
    local_address = models.CharField(max_length=50,null=True,blank=True)
    mobile = PhoneNumberField(unique=True,null=True,blank=True)


    def __str__(self):
        return self.user.username


class Book_Table(models.Model):
      customer  = models.ForeignKey(Customer_Profile,on_delete=models.CASCADE)
      book_date = models.DateField(blank=True)
      book_time = models.TimeField(blank=True)
      place     = models.CharField(max_length=25)


      def __str__(self):
          return self.customer.user.username












