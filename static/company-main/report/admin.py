from django.contrib import admin
from . import models
from .models import DirectHR,  LeaveHRForm ,Monthlyplan,  DrMasterList , Expenses , ChemistMasterList , DailyActivites, DailyDrcallReport, DailyChemistcallReport, DailyDrMeetingReport,Others
# Daily_plan,chemistlist, Dr_visit_report, Expenses, DailyWorkingReport,HQ_List, chemist_call_report, day_summary, RCPA_details, doctor_visit_report
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class DirectHRAdmin(ModelAdmin):
	list_display = ['user','message']
	search_field = ['user','message']
	list_filter = [ 'user','message' ]
admin.site.register(DirectHR, DirectHRAdmin)




class OthersAdmin(ModelAdmin):
	list_display = ['user','text']
	search_field = ['user','text']
	list_filter = [ 'user','text' ]
admin.site.register(Others, OthersAdmin)


class  MonthlyplanAdmin(ModelAdmin):
	list_display = ['user', 'doctor_name' , 'plan_date' , 'is_rejected' , "is_approved"]
	search_field = ['user', 'doctor_name' , 'plan_date' , 'is_rejected' , "is_approved"]
	list_filter = ['user', 'doctor_name' , 'plan_date' , 'is_rejected' , "is_approved"]
admin.site.register( Monthlyplan, MonthlyplanAdmin)




class DailyDrcallReportAdmin(ModelAdmin):
	list_display = ['user' , 'dr_name' ,'dr_speciality', 'workwith']
	search_field = ['user' , 'dr_name' ,'dr_speciality', 'workwith']
	list_filter = [ 'user' , 'dr_name' ,'dr_speciality', 'workwith' ]
admin.site.register(DailyDrcallReport, DailyDrcallReportAdmin)



class DailyChemistcallReportAdmin(ModelAdmin):
	list_display = ['user' , 'chemist_name' ]
	search_field = ['user' , 'chemist_name' ]
	list_filter = [ 'user' , 'chemist_name'  ]
admin.site.register(DailyChemistcallReport, DailyChemistcallReportAdmin)



class DailyDrMeetingReportAdmin(ModelAdmin):
	list_display = ['user','dr_name' , 'dr_speciality']
	search_field = ['user','dr_name', 'dr_speciality']
	list_filter = [ 'user','dr_name' , 'dr_speciality' ]
admin.site.register(DailyDrMeetingReport, DailyDrMeetingReportAdmin)

class LeaveHRFormAdmin(ModelAdmin):
	list_display = ['user','reason']
	search_field = ['user','reason']
	list_filter = [ 'user','reason' ]
admin.site.register( LeaveHRForm,  LeaveHRFormAdmin)

class  DrMasterListAdmin(ModelAdmin):
	list_display = ['user','dr_name', 'city', 'dr_speciality']
	search_field = ['user', 'dr_name']
	list_filter = ['user', 'dr_name', 'city']	
admin.site.register( DrMasterList,  DrMasterListAdmin)

class  ChemistMasterListAdmin(ModelAdmin):
	list_display = ['user','chemist_name', 'city', 'mobile']
	search_field = ['user', 'chemist_name']
	list_filter = ['user', 'chemist_name', 'city']	
admin.site.register( ChemistMasterList,  ChemistMasterListAdmin)


class  DailyActivitesAdmin(ModelAdmin):
	list_display = ['user','is_field' , 'is_meeting', 'is_workFromHome', 'is_other', 'is_adminDay', 'is_covid19']
	search_field = ['user','is_field' , 'is_meeting', 'is_workFromHome', 'is_other', 'is_adminDay', 'is_covid19']
	list_filter = ['user','is_field' , 'is_meeting', 'is_workFromHome', 'is_other', 'is_adminDay', 'is_covid19'	]
admin.site.register( DailyActivites, DailyActivitesAdmin)

class ExpensesAdmin(ModelAdmin):
	list_display = ['user', 'date' , 'chemist_meeting', 'total_appointment']
	search_field = ['user']
	list_filter = ['user']
admin.site.register(Expenses, ExpensesAdmin)

"""
class Daily_planAdmin(ModelAdmin):
	list_display = ['user', 'day','date']
	search_field = ['user', 'day']
	list_filter = ['user', 'day']	
admin.site.register(Daily_plan,Daily_planAdmin)

class Dr_visit_reportAdmin(ModelAdmin):
	list_display = ['user', 'dr_name', 'visit_date' ,  'dr_speciality' , 'city', 'place']
	search_field = ['user', 'dr_name', 'dr_speciality']
	list_filter = ['user', 'dr_name', 'city', 'visit_date']
	
admin.site.register(Dr_visit_report, Dr_visit_reportAdmin)

class ExpensesAdmin(ModelAdmin):
	list_display = ['user', 'date' , 'working_place','chemist_meeting', 'total_appointment']
	search_field = ['user']
	list_filter = ['user']
admin.site.register(Expenses, ExpensesAdmin)

class DailyWorkingReportAdmin(ModelAdmin):
	list_display = ['user', 'dr_name','meeting_place', 'Date_time' , 'current_month_business', 'Daily_business_outcomes']
	search_field = ['user', 'dr_name']
	list_filter = ['user', 'dr_name']
	
admin.site.register(DailyWorkingReport, DailyWorkingReportAdmin)

class chemist_call_reportAdmin(ModelAdmin):
	list_display = ['user', 'chemist_name','business_outcomes_chemist_visit' , 'date_of_visit']
	search_field = ['user', 'chemist_name']
	list_filter = ['user', 'chemist_name']
	
admin.site.register(chemist_call_report, chemist_call_reportAdmin)

class day_summaryAdmin(ModelAdmin):
	list_display = ['user', 'total_calls','total_chemist_meeting', 'report_submission']
	search_field = ['user']
	list_filter = ['user', 'report_submission']
	
admin.site.register(day_summary, day_summaryAdmin)

class RCPA_detailsAdmin(ModelAdmin):
	list_display = ['user', 'brand_name', 'date_of_visit']
	search_field = ['user', 'brand_name']
	list_filter = ['user','brand_name']
	
admin.site.register(RCPA_details,RCPA_detailsAdmin)

class doctor_visit_reportAdmin(ModelAdmin):
	list_display = ['user', 'doctor_name','date_of_visit', 'month']
	search_field = ['user', 'doctor_name']
	list_filter = ['user', 'doctor_name', 'date_of_visit', 'month']
	
admin.site.register(doctor_visit_report, doctor_visit_reportAdmin)

class HQ_ListAdmin(ModelAdmin):
	list_display = ['user', 'dr_name','date', 'place', 'current_doctor_business',
	 'current_prescribing_brand', 'brand_name1', 'brand_name2' ,
	  'brand_name3', 'brand_name4', 'brand_name5']
	search_field = ['user', 'dr_name','date', 'place']
	list_filter = ['user', 'dr_name','date', 'place']
	
admin.site.register(HQ_List, HQ_ListAdmin)

class chemistlistAdmin(ModelAdmin):
	list_display = ['user', 'chemist_name','date', 'place', 'contact',
	 'POB_Collection_status','ABM_Approach_Status', 'brand_name1', 'brand_name2' ,
	  'brand_name3']
	search_field = ['user', 'chemist_name','date', 'place', 'contact']
	list_filter = ['user', 'chemist_name','date', 'place', 'contact']
	
admin.site.register(chemistlist, chemistlistAdmin)




#just for demo purpose 
# Register your models here.
"""
