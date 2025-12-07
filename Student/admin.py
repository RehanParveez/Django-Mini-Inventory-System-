from django.contrib import admin
from Student.models import Products

# Register your models here.
admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'category']
    