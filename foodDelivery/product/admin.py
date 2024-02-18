from django.contrib import admin

# Register your models here.
# app/admin.py

from .models import Category 

admin.site.register(Category)
from .models import CompanyInformation 

admin.site.register(CompanyInformation)
from .models import Product 

admin.site.register(Product) 
