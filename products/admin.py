from django.contrib import admin
from .models import *

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name",'image', "description","type","price"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["products",'quantity', "status", "date_created"]

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]

admin.site.register(Products,ProductsAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(AboutUs,AboutUsAdmin)


