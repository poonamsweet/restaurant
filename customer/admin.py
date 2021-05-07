from django.contrib import admin
from .models import  User,Customer_Profile,Book_Table

# Register your models here.
admin.site.register(Customer_Profile)
admin.site.register(User)
admin.site.register(Book_Table)


