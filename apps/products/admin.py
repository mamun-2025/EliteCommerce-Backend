from django.contrib import admin
from .models import Category, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('name',)} # নাম লিখলে অটো স্লাগ তৈরি হবে

admin.site.register(Brand)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ('name', 'price', 'category', 'stock', 'created_at')
   list_filter = ('category', 'brand')
   search_fields = ('name', 'description')

   

