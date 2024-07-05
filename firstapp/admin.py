from django.contrib import admin
from .models import Products
from rest_framework_api_key.models import APIKey
# Register your models here.
class Product_admin(admin.ModelAdmin):
    list_display = ['id','name','prize','quantity','category','bill','add_to_cart','image','user']
admin.site.register(Products,Product_admin)
