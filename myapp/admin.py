from django.contrib import admin
from myapp.models import Product
# Register your models here.
# class ProductAdmin(admin.ModelAdmin):
admin.site.register(Product)
