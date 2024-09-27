from django.contrib import admin
from app.models import (
  GeneralInfo,                       
  Service, 
  Testimonial, 
  FrequentlyAskedQuestion,
  ContactFormLog,
  ) #you call the model

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):

  list_display = [
    'company_name',
    'location',
    'email',
    'phone',
    'open_hours',
  ]

# # show to disable add permission
# def has_add_permission(self, request, obj=None):
#     return False

# # show to disable update permission
# def has_change_permission(self, request, obj=None):
#     return False

# # show to disable delete permission
# def has_delete_permission(self, request, obj=None):
#     return False

# show you can set field to disable update

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
  list_display = [
    'title',
    'description',
  ]

  search_fields = [
    'title',
  ]

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
  list_display = [
    'username',
    'user_job_title',
    'display_rating_count',
  ]

  def display_rating_count(self, obj):
    return '*' * obj.rating_count 
  
  display_rating_count.sort_description = "Rating"

@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
  list_display = [
  'question',
  'answer',
]
  
@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):

  list_display = [
    'email',
    'is_success',
    'is_error',
    'action_time',
  ]
# esta parte es para evitar modificar la seccion de logs descomenta para quitar permisos
  # def has_add_permission(self, request, obj=None):
  #       return False

  # def has_change_permission(self, request, obj=None):
  #       return False

  # def has_delete_permission(self, request, obj=None):
  #       return False
