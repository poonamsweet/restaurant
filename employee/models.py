from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from customer.models import User

# Create your models here.


GENDER_CHOICES = (
    ('Select', 'Select'),
    ('Male', 'Male'),
    ('Female', 'Female'),

)
profile_CHOICES = (
    ('Select', 'Select'),
    ('Cook', 'Cook'),
    ('Waiter', 'Waiter'),
    ('Staff', 'Staff'),
)




class Employee_Profile(models.Model):
    user    = models.OneToOneField(User,on_delete = models.CASCADE ,null=True)
    profile = models.CharField(max_length=32,choices=profile_CHOICES,default="select",null=True,blank=True)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    gender = models.CharField(max_length=32, choices=GENDER_CHOICES, default="select",null=True,blank=True)
    dateofbirth = models.DateField(null=True,blank=True)
    present_location = models.CharField(max_length=30,null=True,blank=True)
    permanent_address = models.CharField(max_length=50,null=True,blank=True)
    local_address = models.CharField(max_length=50,null=True,blank=True)
    mobile = PhoneNumberField(unique=True,null=True,blank=True)

    def __str__(self):
        return f'{self.user.username}'


class  Staff_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=32, choices=GENDER_CHOICES, default="select")
    dateofbirth = models.DateField()
    present_location = models.CharField(max_length=30)
    permanent_address = models.CharField(max_length=50)
    local_address = models.CharField(max_length=50)
    mobile = PhoneNumberField(unique=True)



class EntryExit(models.Model):
     employeename = models.CharField(max_length=35)
     entry_time   = models.TimeField()
     exit_time    = models.TimeField()
     totol_hour   = models.IntegerField()

     def __str__(self):
         return self.employeename





