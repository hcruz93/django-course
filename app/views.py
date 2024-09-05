from django.shortcuts import render
from app.models import GeneralInfo
from django.db.models import Q
from django.db import connection

def writes_sql_queries_to_file(file_path):
  with open(file_path,'w') as file:
    queries = connection.queries
    for query in queries:
      sql = query['sql'] 
      file.write(f"{sql}\n")

# Create your views here.
def index(request):

  # #READ
  # all_records = GeneralInfo.objects.all()
  # print(all_records)
  
  # first_record = GeneralInfo.objects.first()
  # print(first_record)

  # last_five_record = GeneralInfo.objects.all().order_by('-id')[:5]
  # for i in last_five_record:
  #   print(i.location)


  # #DELETE
  # GeneralInfo.objects.filter(company_name="Company").delete()

  # #UPDATE
  # company = GeneralInfo.objects.get(id=1)
  # company.phone = "56145677"
  # company.save()

  # company = GeneralInfo.objects.all().update(phone = " 741585585")

  # #CREATE
  # GeneralInfo.objects.create (
  #   company_name = "Samsung",
  #   location= "asia",
  #   phone = "8528525",
  #   email = "fghj@example.com"

  # )



  file_path = 'sql_queries.txt'
  writes_sql_queries_to_file(file_path)

  context = {}


  return render(request,"index.html",context)

