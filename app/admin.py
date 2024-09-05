from django.contrib import admin
from django.http import HttpRequest

# Register your models here.
from app.models import GeneralInfo #you call the model

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):

  list_display = [
    'company_name',
    'location',
    'email',
    'phone',
    'open_hours',
  ]

# PERMITIR O BLOQUEAR AGREGAR ACTUALLIZAR O BORRAR UN REGISTRO

  #show to disable and permission
  # def has_add_permission(self, request, obj=None):
  #   return False

  #show to disable updated permissions
  # def has_change_permission(self, request, obj=None):
  #   return False
  
  # show to disable deleted permission
  # def has_delete_permission(self, request, obj=None):
  #   return False
