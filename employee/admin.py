from django.contrib import admin
from .models import Employee_Profile





class Employee_ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','image', 'dateofbirth', 'present_location','permanent_address','local_address','mobile')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True


admin.site.register(Employee_Profile, Employee_ProfileAdmin)
