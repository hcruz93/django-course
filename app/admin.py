from django.contrib import admin
from app.models import GeneralInfo, Service #you call the model

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):

  list_display = [
    'company_name',
    'location',
    'email',
    'phone',
    'open_hours',
  ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = [
    'title',
    'description',
  ]

  search_fields = [
    'title',
  ]

