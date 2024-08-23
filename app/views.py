from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
  context = {
    'course_title': 'Django Course',
    'current_date': datetime.now(),
    'user': {
      'name': 'Humberto Cruz',
      'email': 'hum.alex@gmail.com',
    },
    'product_price': 199.93999,
    'random_text': 'ahhhh ahhh bueno esta bieeeeen'
  }
  return render(request,"index.html",context)

