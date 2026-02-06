
from rest_framework import serializers
from .models import Category, Brand, Product

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = ['id', 'name', 'slug']

class BrandSerializer(serializers.ModelSerializer):
   class Meta:
      model = Brand
      fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
   category = CategorySerializer(read_only=True)
   brand = BrandSerializer(read_only=True)
   class Meta:
      model = Product
      fields = [
         'id',
         'name',
         'description',
         'price',
         'stock',
         'category',
         'brand',
         'image',
         'created_at'
      ]



