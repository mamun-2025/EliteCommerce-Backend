
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryListView(generics.ListAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer

class ProductListView(generics.ListAPIView):
   queryset = Product.objects.select_related('category', 'brand').all()
   serializer_class = ProductSerializer

   # এখানে ৩টি ব্যাকএন্ড যোগ করছি: সাধারণ ফিল্টার, সার্চ এবং অর্ডারিং
   filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

   # ১. ক্যাটাগরি এবং ব্র্যান্ড আইডি দিয়ে ফিল্টার করার জন্য
   filterest_fields = ['category', 'brand']

   # ২. নাম এবং ডেসক্রিপশন দিয়ে সার্চ করার জন্য
   search_fields = ['name', 'description']

   # ৩. দাম এবং তৈরির তারিখ অনুযায়ী সাজানোর (Sort) জন্য
   ordering_fields = ['price', 'created_at']
   
class ProductDetailView(generics.RetrieveAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializer
   lookup_field = 'id' # ডিফল্টভাবে এটি 'pk' থাকে, আমরা 'id' হিসেবেও সেট করতে পারি
   
















 