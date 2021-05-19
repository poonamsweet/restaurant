
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	is_se = models.BooleanField(default = False)
	is_abm = models.BooleanField(default = False)
	is_rbm = models.BooleanField(default = False)
	is_zbm = models.BooleanField(default = False)
	is_admin = models.BooleanField(default = False)
	username = models.CharField(max_length = 15,unique=True)
	first_name = models.CharField(max_length = 15)
	last_name = models.CharField(max_length = 15)
	email = models.EmailField()
	mobile_number = models.CharField(max_length = 15 ,null = True , blank = True)


CATEGORY_CHOICES = (
	('Select', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
CATEGORY_MARRIED_CHOICES = (
	('select', 'Select'),
        ('Married', 'Married'),
        ('Single', 'Single'),
    )
    
EXPERIENCE_CHOICES = (
	('select', 'Select'),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    
MAILING_CHOICES = (
	('select', 'Select'),
        ('Same', 'Same'),
        ('Different', 'Different'),
    )




class Salesexecutive(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE ,null=True)	
	location = models.CharField(max_length = 50 , null = True , blank = True)
	birthdate = models.DateField(auto_now_add= True )
	gender = models.CharField(max_length=10, choices=CATEGORY_CHOICES )
	height = models.CharField(max_length = 8 , null = True , blank = True)
	weight = models.CharField(max_length = 7 , null = True , blank = True)
	identification_mark = models.CharField(max_length = 50 , null = True , blank = True)
	blood_group = models.CharField(max_length = 3 , null = True , blank = True)
	maritual_status  = models.CharField(max_length =20 , choices = CATEGORY_MARRIED_CHOICES )
	marriage_date = models.DateField(auto_now_add= True )
	Nationality = models.CharField(max_length=6)

	address_line_1 = models.CharField(max_length=30)
	address_line_2 = models.CharField(max_length=30)
	pin = models.CharField(max_length=6)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=30)

	mailing_address =  models.CharField(max_length=20,choices=MAILING_CHOICES)
	mail_address_line_1 = models.CharField(max_length=30)
	mail_address_line_2 = models.CharField(max_length=30)
	mail_pin = models.CharField(max_length=6)
	mail_city = models.CharField(max_length=15)
	mail_state = models.CharField(max_length=30)
	
	bank_name         = models.CharField(max_length=20)
	account_no        = models.CharField(max_length=20)
	pan_no            = models.CharField(max_length=20)
	pan_pic           = models.ImageField()
	passport_no       = models.CharField(max_length=20)
	passport_pic =     models.FileField()
	driving_license   = models.CharField(max_length=20)
	driving_license_pic =  models.FileField()

	high_school       = models.CharField(max_length=30)
	high_school_passing_year   = models.CharField(max_length=4)
	high_school_marks_obtained    = models.CharField(max_length=5)
	high_school_cert =            models.FileField()

	intermediate_school       = models.CharField(max_length=30)
	intermediate_passing_year   = models.CharField(max_length=5)
	intermediate_marks_obtained    = models.CharField(max_length=4)	
	intermediate_cert =           models.FileField()

	Degree_obtained = models.CharField(max_length=30)
	college_institute = models.CharField(max_length=50)
	Year_of_passing   = models.CharField(max_length=4)
	marks_obtained    = models.CharField(max_length=5)
	degree_cert = models.FileField()



	experience         = models.CharField(max_length=20,choices=EXPERIENCE_CHOICES)
	organisation_name = models.CharField(max_length=50)
	position_held     = models.CharField(max_length=20)
	head_quater       = models.CharField(max_length=50)
	date_of_joining   = models.DateField(null=True,blank=True)
	date_of_leaving   = models.DateField(null=True,blank=True)
	father_name       = models.CharField(max_length=20)
	mother_name       = models.CharField(max_length=20)
	brother          = models.CharField(max_length=1)
	sister            = models.CharField(max_length=1)
	spouse_name      = models.CharField(max_length=20)  
	children_count     = models.CharField(max_length=1)



	def __str__(self):
		return f'{self.user.username}'	


class Abm(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE , primary_key = True)
	area = models.CharField(max_length = 15)
	birthdate = models.DateField(auto_now_add= True )
	gender = models.CharField(max_length=10, choices=CATEGORY_CHOICES )
	height = models.CharField(max_length = 8 , null = True , blank = True)
	weight = models.CharField(max_length = 7 , null = True , blank = True)
	identification_mark = models.CharField(max_length = 50 , null = True , blank = True)
	blood_group = models.CharField(max_length = 3 , null = True , blank = True)
	maritual_status  = models.CharField(max_length =20 , choices = CATEGORY_MARRIED_CHOICES )
	marriage_date = models.DateField(auto_now_add= True )
	Nationality = models.CharField(max_length=6)

	address_line_1 = models.CharField(max_length=30)
	address_line_2 = models.CharField(max_length=30)
	pin = models.CharField(max_length=6)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=30)

	mailing_address =  models.CharField(max_length=20,choices=MAILING_CHOICES)
	mail_address_line_1 = models.CharField(max_length=30)
	mail_address_line_2 = models.CharField(max_length=30)
	mail_pin = models.CharField(max_length=6)
	mail_city = models.CharField(max_length=15)
	mail_state = models.CharField(max_length=30)
	
	bank_name         = models.CharField(max_length=20)
	account_no        = models.CharField(max_length=20)
	pan_no            = models.CharField(max_length=20)
	pan_pic           = models.ImageField()
	passport_no       = models.CharField(max_length=20)
	passport_pic =     models.FileField()
	driving_license   = models.CharField(max_length=20)
	driving_license_pic =  models.FileField()

	high_school       = models.CharField(max_length=30)
	high_school_passing_year   = models.CharField(max_length=4)
	high_school_marks_obtained    = models.CharField(max_length=5)
	high_school_cert =            models.FileField()

	intermediate_school       = models.CharField(max_length=30)
	intermediate_passing_year   = models.CharField(max_length=4)
	intermediate_marks_obtained    = models.CharField(max_length=5)	
	intermediate_cert =           models.FileField()

	Degree_obtained = models.CharField(max_length=30)
	college_institute = models.CharField(max_length=50)
	Year_of_passing   = models.CharField(max_length=4)
	marks_obtained    = models.CharField(max_length=5)
	degree_cert = models.FileField()



	experience         = models.CharField(max_length=20,choices=EXPERIENCE_CHOICES)
	organisation_name = models.CharField(max_length=50)
	position_held     = models.CharField(max_length=20)
	head_quater                = models.CharField(max_length=50)
	date_of_joining   = models.DateField(null=True,blank=True)
	date_of_leaving   = models.DateField(null=True,blank=True)
	father_name       = models.CharField(max_length=20)
	mother_name       = models.CharField(max_length=20)
	brother          = models.CharField(max_length=1)
	sister            = models.CharField(max_length=1)
	spouse_name      = models.CharField(max_length=20)  
	children_count     = models.CharField(max_length=1)



	


	def __str__(self):
		return f'{self.user.username}'

class Rbm(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE , primary_key = True)
	region = models.CharField(max_length = 15 , null = True , blank = True)

	birthdate = models.DateField(auto_now_add= True )
	gender = models.CharField(max_length=10, choices=CATEGORY_CHOICES )
	height = models.CharField(max_length = 8 , null = True , blank = True)
	weight = models.CharField(max_length = 7 , null = True , blank = True)
	identification_mark = models.CharField(max_length = 50 , null = True , blank = True)
	blood_group = models.CharField(max_length = 3 , null = True , blank = True)
	maritual_status  = models.CharField(max_length =20 , choices = CATEGORY_MARRIED_CHOICES )
	marriage_date = models.DateField(auto_now_add= True )
	Nationality = models.CharField(max_length=6)

	address_line_1 = models.CharField(max_length=30)
	address_line_2 = models.CharField(max_length=30)
	pin = models.CharField(max_length=6)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=30)

	mailing_address =  models.CharField(max_length=20,choices=MAILING_CHOICES)
	mail_address_line_1 = models.CharField(max_length=30)
	mail_address_line_2 = models.CharField(max_length=30)
	mail_pin = models.CharField(max_length=6)
	mail_city = models.CharField(max_length=15)
	mail_state = models.CharField(max_length=30)
	
	bank_name         = models.CharField(max_length=20)
	account_no        = models.CharField(max_length=20)
	pan_no            = models.CharField(max_length=20)
	pan_pic           = models.ImageField()
	passport_no       = models.CharField(max_length=20)
	passport_pic =     models.FileField()
	driving_license   = models.CharField(max_length=20)
	driving_license_pic =  models.FileField()

	high_school       = models.CharField(max_length=30)
	high_school_passing_year   = models.CharField(max_length=4)
	high_school_marks_obtained    = models.CharField(max_length=5)
	high_school_cert =            models.FileField()

	intermediate_school       = models.CharField(max_length=30)
	intermediate_passing_year   = models.CharField(max_length=4)
	intermediate_marks_obtained    = models.CharField(max_length=5)	
	intermediate_cert =           models.FileField()

	Degree_obtained = models.CharField(max_length=30)
	college_institute = models.CharField(max_length=50)
	Year_of_passing   = models.CharField(max_length=4)
	marks_obtained    = models.CharField(max_length=5)
	degree_cert = models.FileField()



	experience         = models.CharField(max_length=20,choices=EXPERIENCE_CHOICES)
	organisation_name = models.CharField(max_length=50)
	position_held     = models.CharField(max_length=20)
	head_quater                = models.CharField(max_length=50)
	date_of_joining   = models.DateField(null=True,blank=True)
	date_of_leaving   = models.DateField(null=True,blank=True)
	father_name       = models.CharField(max_length=20)
	mother_name       = models.CharField(max_length=20)
	brother          = models.CharField(max_length=1)
	sister            = models.CharField(max_length=1)
	spouse_name      = models.CharField(max_length=20)  
	children_count     = models.CharField(max_length=1)



	def __str__(self):
		return f'{self.user.username}'

class Zbm(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE , primary_key = True)
	zone = models.CharField(max_length = 15 , null = True , blank = True)

	birthdate = models.DateField(auto_now_add= True )
	gender = models.CharField(max_length=10, choices=CATEGORY_CHOICES )
	height = models.CharField(max_length = 8 , null = True , blank = True)
	weight = models.CharField(max_length = 7 , null = True , blank = True)
	identification_mark = models.CharField(max_length = 50 , null = True , blank = True)
	blood_group = models.CharField(max_length = 3 , null = True , blank = True)
	maritual_status  = models.CharField(max_length =20 , choices = CATEGORY_MARRIED_CHOICES )
	marriage_date = models.DateField(auto_now_add= True )
	Nationality = models.CharField(max_length=6)

	address_line_1 = models.CharField(max_length=30)
	address_line_2 = models.CharField(max_length=30)
	pin = models.CharField(max_length=6)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=30)

	mailing_address =  models.CharField(max_length=20,choices=MAILING_CHOICES)
	mail_address_line_1 = models.CharField(max_length=30)
	mail_address_line_2 = models.CharField(max_length=30)
	mail_pin = models.CharField(max_length=6)
	mail_city = models.CharField(max_length=15)
	mail_state = models.CharField(max_length=30)
	
	bank_name         = models.CharField(max_length=20)
	account_no        = models.CharField(max_length=20)
	pan_no            = models.CharField(max_length=20)
	pan_pic           = models.ImageField()
	passport_no       = models.CharField(max_length=20)
	passport_pic =     models.FileField()
	driving_license   = models.CharField(max_length=20)
	driving_license_pic =  models.FileField()

	high_school       = models.CharField(max_length=30)
	high_school_passing_year   = models.CharField(max_length=4)
	high_school_marks_obtained    = models.CharField(max_length=5)
	high_school_cert =            models.FileField()

	intermediate_school       = models.CharField(max_length=30)
	intermediate_passing_year   = models.CharField(max_length=4)
	intermediate_marks_obtained    = models.CharField(max_length=5)	
	intermediate_cert =           models.FileField()

	Degree_obtained = models.CharField(max_length=30)
	college_institute = models.CharField(max_length=50)
	Year_of_passing   = models.CharField(max_length=4)
	marks_obtained    = models.CharField(max_length=5)
	degree_cert = models.FileField()



	experience         = models.CharField(max_length=20,choices=EXPERIENCE_CHOICES)
	organisation_name = models.CharField(max_length=50)
	position_held     = models.CharField(max_length=20)
	head_quater                = models.CharField(max_length=50)
	date_of_joining   = models.DateField(null=True,blank=True)
	date_of_leaving   = models.DateField(null=True,blank=True)
	father_name       = models.CharField(max_length=20)
	mother_name       = models.CharField(max_length=20)
	brother          = models.CharField(max_length=1)
	sister            = models.CharField(max_length=1)
	spouse_name      = models.CharField(max_length=20)  
	children_count     = models.CharField(max_length=1)


	def __str__(self):
		return f'{self.user.username}'


class Admin(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE , primary_key = True)
	company = models.CharField(max_length = 15 , null = True , blank = True)


	birthdate = models.DateField(auto_now_add= True )
	gender = models.CharField(max_length=10, choices=CATEGORY_CHOICES )
	height = models.CharField(max_length = 8 , null = True , blank = True)
	weight = models.CharField(max_length = 7 , null = True , blank = True)
	identification_mark = models.CharField(max_length = 50 , null = True , blank = True)
	blood_group = models.CharField(max_length = 3 , null = True , blank = True)
	maritual_status  = models.CharField(max_length =20 , choices = CATEGORY_MARRIED_CHOICES )
	marriage_date = models.DateField(auto_now_add= True )
	Nationality = models.CharField(max_length=6)

	address_line_1 = models.CharField(max_length=30)
	address_line_2 = models.CharField(max_length=30)
	pin = models.CharField(max_length=6)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=30)

	mailing_address =  models.CharField(max_length=20,choices=MAILING_CHOICES)
	mail_address_line_1 = models.CharField(max_length=30)
	mail_address_line_2 = models.CharField(max_length=30)
	mail_pin = models.CharField(max_length=6)
	mail_city = models.CharField(max_length=15)
	mail_state = models.CharField(max_length=30)
	
	bank_name         = models.CharField(max_length=20)
	account_no        = models.CharField(max_length=20)
	pan_no            = models.CharField(max_length=20)
	pan_pic           = models.ImageField()
	passport_no       = models.CharField(max_length=20)
	passport_pic =     models.FileField()
	driving_license   = models.CharField(max_length=20)
	driving_license_pic =  models.FileField()

	high_school       = models.CharField(max_length=30)
	high_school_passing_year   = models.CharField(max_length=4)
	high_school_marks_obtained    = models.CharField(max_length=5)
	high_school_cert =            models.FileField()

	intermediate_school       = models.CharField(max_length=30)
	intermediate_passing_year   = models.CharField(max_length=4)
	intermediate_marks_obtained    = models.CharField(max_length=5)	
	intermediate_cert =           models.FileField()

	Degree_obtained = models.CharField(max_length=30)
	college_institute = models.CharField(max_length=50)
	Year_of_passing   = models.CharField(max_length=4)
	marks_obtained    = models.CharField(max_length=5)
	degree_cert = models.FileField()



	experience         = models.CharField(max_length=20,choices=EXPERIENCE_CHOICES)
	organisation_name = models.CharField(max_length=50)
	position_held     = models.CharField(max_length=20)
	head_quater                = models.CharField(max_length=50)
	date_of_joining   = models.DateField(null=True,blank=True)
	date_of_leaving   = models.DateField(null=True,blank=True)
	father_name       = models.CharField(max_length=20)
	mother_name       = models.CharField(max_length=20)
	brother          = models.CharField(max_length=1)
	sister            = models.CharField(max_length=1)
	spouse_name      = models.CharField(max_length=20)  
	children_count     = models.CharField(max_length=1)


	def __str__(self):
		return f'{self.user.username}'








