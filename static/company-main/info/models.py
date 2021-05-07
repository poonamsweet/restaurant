from django.db import models
from django.utils import timezone


# Create your models here.

class Contact(models.Model):
	first_name = models.CharField(max_length = 100)
	second_name = models.CharField(max_length = 100)
	email = models.EmailField() 
	mobile = models.CharField(max_length = 10)
	message = models.TextField()
	date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.first_name 

class Gallary(models.Model):
	image = models.ImageField()
	about = models.CharField(max_length= 50 )
	text = models.CharField(max_length=100)

	def __str__(self):
		return self.about 


	@property
	def mediaURL(self):
		try : 
			url = self.image.url
		except : 
			url = ''
		return url 
