from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
  products = [
    {'Name': 'Laptop', 'Price': 778.98},
    {'Name': 'Smartphone', 'Price': 578.98},
    {'Name': 'Headphones', 'Price': 52.98},
    {'Name': 'Camera', 'Price': 89.98},
  ]
  context = {
    'products': products,
  }
  return render(request,"index.html",context)

