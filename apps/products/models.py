from django.db import models

# ক্যাটাগরি মডেল (যেমন: ইলেকট্রনিক্স, ফ্যাশন)
class Category(models.Model):
   name = models.CharField(max_length=100, unique=True)
   slug = models.SlugField(max_length=120, unique=True)
   description = models.TextField(blank=True)

   class Meta:
      verbose_name_plural = "Categories"

   def __str__(self):
      return self.name

# ব্র্যান্ড মডেল (যেমন: Apple, Samsung)
class Brand(models.Model):
   name = models.CharField(max_length=100, unique=True)
   description = models.TextField(blank=True)

   def __str__(self):
      return self.name 

# মেইন প্রোডাক্ট মডেল
class Product(models.Model):
   category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
   brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
   name = models.CharField(max_length=255)   
   description = models.TextField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   stock = models.PositiveIntegerField(default=0)
   image = models.ImageField(upload_to='products/', null=True, blank=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.name 


