from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'color', 'created_date', 'in_stock')

admin.site.register(Product, ProductAdmin)
