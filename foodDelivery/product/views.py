from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here
 
# def home(request):
#     return render(request, 'home.html')
# def about(request):
#         return render(request, 'about.html')
# def contact_us(request):
#     return render(request, 'contact_us.html')
# def product(request): 
#         return render(request, 'features.html')

def home(request):
   info = CompanyInformation.objects.all().first()
   # Retrieve the first four products
   products = Product.objects.all()[:4]

   data = {
      'info': info, 
      'products': products

   }
   return render(request,'home.html', data)
   
   
def about(request):
   return render(request , 'about.html')

def product(request):
   
   all_products = Product.objects.all()

   data_all = {
      'products': all_products

   }
   return render(request , 'features.html' , data_all)
   
def contact_us(request):
      return render(request , 'contact_us.html')
  