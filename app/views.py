from django.shortcuts import render
from app.models import GeneralInfo , Service, Testimonial, FrequentlyAskedQuestion

# Create your views here.
def index(request):
  general_info = GeneralInfo.objects.first()
  services = Service.objects.all() # you bring all the services
  testimonials = Testimonial.objects.all()
  faqs = FrequentlyAskedQuestion.objects.all()

  contex = {
    "company_name": general_info.company_name,
    "location": general_info.location,
    "email": general_info.email,
    "phone": general_info.phone,
    "open_hours": general_info.open_hours,
    "video_url": general_info.video_url,
    "facebook_url": general_info.facebook_url,
    "instagram_url": general_info.instagram_url,
    "linkedin_url": general_info.linkedin_url,

    "services" : services,
    "testimonials" : testimonials,
    "faqs": faqs,
  }

  return render (request, "index.html",contex) 