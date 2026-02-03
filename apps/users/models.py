from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# ১. কাস্টম ইউজার ম্যানেজার
# ডিফল্টভাবে জ্যাঙ্গো 'username' দিয়ে লগইন করায়। আমরা যেহেতু 'email' দিয়ে লগইন করাতে চাই, 
# তাই আমাদের নিজেদের মতো করে ইউজার তৈরির লজিক লিখতে হয়।
class CustomUserManager(BaseUserManager):

   # সাধারণ ইউজার তৈরি করার মেথড
   def create_user(self, email, password=None, **extra_fields):
      if not email:
         raise ValueError("Users must have an email address.")
      
      # ইমেইল নরমালাইজ করা (যেমন: Gmail.com কে gmail.com করা)
      email = self.normalize_email(email)
      # ইউজার অবজেক্ট তৈরি করা
      user = self.model(email=email, **extra_fields)
      # পাসওয়ার্ডকে হ্যাশ (Hash) করে সেভ করা (নিরাপত্তার জন্য সরাসরি টেক্সট সেভ হয় না)
      user.set_password(password)
      # ডাটাবেসে সেভ করা
      user.save(using=self._db)
      return user

   # অ্যাডমিন বা সুপারইউজার তৈরি করার মেথড
   def create_superuser(self, email, password=None, **extra_fields):
      # সুপারইউজারের জন্য এই ফিল্ডগুলো অবশ্যই True হতে হবে
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      return self.create_user(email, password, **extra_fields)
   

# ২. কাস্টম ইউজার মডেল
# AbstractBaseUser: একদম শুরু থেকে ইউজার মডেল তৈরির ক্ষমতা দেয়।
# PermissionsMixin: জ্যাঙ্গোর গ্রুপ এবং পারমিশন সিস্টেম ব্যবহার করার সুবিধা দেয়।
class User(AbstractBaseUser, PermissionsMixin):
   email = models.EmailField(unique=True) # ইমেইল ইউনিক হবে যাতে একই ইমেইল দিয়ে দুটি আইডি না হয়
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)

   # স্ট্যাটাস ফিল্ডস
   is_active = models.BooleanField(default=True) # ইউজার একটিভ কিনা
   is_staff = models.BooleanField(default=False) # সে অ্যাডমিন প্যানেলে ঢুকতে পারবে কিনা

   # PermissionsMixin থেকে এটি অটোমেটিক আসে, তবে আপনি চাইলে ম্যানুয়ালি লিখতে পারেন:
   is_superuser = models.BooleanField(default=False) # এটি নির্ধারণ করে ইউজারের সব পারমিশন আছে কিনা। 
   # সাধারণত সুপারইউজার তৈরির সময় এটি True করে দেওয়া হয়।

   # উপরে তৈরি করা ম্যানেজারকে এই মডেলের সাথে কানেক্ট করা
   objects = CustomUserManager()
   
   # লগইন করার সময় ইউজারনেমের বদলে ইমেইল ব্যবহার হবে
   USERNAME_FIELD = 'email'

   # সুপারইউজার ক্রিয়েট করার সময় ইমেইল আর পাসওয়ার্ড বাদে আর কি কি লাগবে
   REQUIRED_FIELDS = ['first_name', 'last_name']

   def __str__(self):
      return self.email
   




# আমরা জ্যাঙ্গোর ডিফল্ট User মডেল ব্যবহার না করে AbstractBaseUser ব্যবহার করব যাতে আমরা ইমেইল দিয়ে লগইন সিস্টেম তৈরি করতে পারি।
# ১. কেন AbstractBaseUser ব্যবহার করছি? (ইন্টারভিউ নোট)
# Customization: ডিফল্ট জ্যাঙ্গো ইউজার মডেলে 'username' বাধ্যতামূলক। 
# কিন্তু প্রফেশনাল ই-কমার্সে আমরা চাই ইউজার তার ইমেইল দিয়ে লগইন করুক। 
# AbstractBaseUser আমাদের সেই পূর্ণ স্বাধীনতা দেয়।
# Cleanliness: ডিফল্ট মডেলের অনেক অপ্রয়োজনীয় ফিল্ড (যেমন: first_name, last_name) আমরা বাদ দিয়ে আমাদের প্রয়োজনমতো ফিল্ড নিতে পারি।

# আপনার দেওয়া কোডটি জ্যাঙ্গোতে একটি Custom User Model তৈরির আদর্শ উদাহরণ। 
# বর্তমানে প্রফেশনাল প্রজেক্টগুলোতে বিল্ট-ইন ইউজার মডেলের বদলে এভাবেই ইমেইল দিয়ে লগইন করার সিস্টেম তৈরি করা হয়।
# নিচে ইন্টারভিউয়ের জন্য প্রতিটি অংশের বিস্তারিত ব্যাখ্যা এবং নোট দেওয়া হলো:
# ১. কেন আমরা Custom User Model ব্যবহার করি?
# জ্যাঙ্গোর ডিফল্ট ইউজার মডেলে লগইন করার জন্য username প্রয়োজন হয়। কিন্তু আধুনিক অ্যাপ্লিকেশনে আমরা সাধারণত email দিয়ে লগইন করতে চাই। 
# এছাড়া ইউজার মডেলে বাড়তি কোনো ফিল্ড (যেমন: ফোন নম্বর বা প্রোফাইল পিকচার) যোগ করার ফ্লেক্সিবিলিটি পেতে এই কাস্টমাইজেশন করা হয়।
# ২. কোডের বিস্তারিত ব্যাখ্যাক) CustomUserManager ক্লাসএটি কোনো ডাটাবেস টেবিল নয়, বরং এটি একটি Helper Class যা ইউজার তৈরি করার লজিক বা পদ্ধতি বলে দেয়।
# create_user: সাধারণ ইউজার তৈরি করার জন্য এটি ব্যবহৃত হয়। 
# এখানে ইমেইল নরমালাইজ করা (যেমন: Gmail.com কে gmail.com করা) এবং পাসওয়ার্ড হ্যাশ করার কাজ করা হয়।
# create_superuser: এটি অ্যাডমিন প্যানেলে লগইন করার জন্য বিশেষ ইউজার তৈরি করে। 
# এখানে is_staff এবং is_superuser ফিল্ডগুলোকে অটোমেটিক True করে দেওয়া হয়।
# খ) User ক্লাস (The Model)এটিই মূল ডাটাবেস টেবিল যা AbstractBaseUser এবং PermissionsMixin কে ইনহেরিট করে।
# AbstractBaseUser: এটি আপনাকে একদম স্ক্র্যাচ থেকে ইউজার মডেল তৈরির সুযোগ দেয়। 
# এটি শুধু পাসওয়ার্ড এবং লাস্ট লগইন ফিল্ড দুটি ডিফল্ট হিসেবে দেয়।PermissionsMixin: এটি ব্যবহার করা হয় যাতে আপনার কাস্টম ইউজারের ওপর জ্যাঙ্গোর পারমিশন সিস্টেম (Groups, Permissions) কাজ করতে পারে।
# USERNAME_FIELD = 'email': এটি জ্যাঙ্গোকে বলে দেয় যে, এখন থেকে ইউজার লগইন করার সময় username এর বদলে email ব্যবহার করবে।
# REQUIRED_FIELDS: যখন আপনি কমান্ড লাইনে createsuperuser লিখবেন, তখন ইমেইল ও পাসওয়ার্ড বাদে আর কোন ফিল্ডগুলো ইনপুট নেওয়া বাধ্যতামূলক হবে, 
# তা এখানে ডিফাইন করা হয়।
# ৩. ইন্টারভিউ নোট (Interview Cheat Sheet)আপনি যদি ইন্টারভিউতে এই কোড নিয়ে প্রশ্নের সম্মুখীন হন, 
# তবে এই পয়েন্টগুলো মনে রাখবেন:
# TopicKey PointWhy normalize_email?
# যাতে User@Gmail.Com এবং user@gmail.com একই ইমেইল হিসেবে গণ্য হয়। 
# এটি ইমেইলের ডোমেইন অংশকে ছোট হাতের অক্ষরে রূপান্তর করে।
# set_password() কেন?সরাসরি পাসওয়ার্ড সেভ করলে সেটি ডাটাবেসে প্লেইন টেক্সট হিসেবে থাকে, যা নিরাপদ নয়। 
# set_password পাসওয়ার্ডকে PBKDF2 অ্যালগরিদমে হ্যাশ করে সেভ করে।
# objects = CustomUserManager()জ্যাঙ্গোর ডিফল্ট কুয়েরি ম্যানেজারকে সরিয়ে আমাদের তৈরি করা কাস্টম ম্যানেজার যুক্ত করা, 
# যাতে User.objects.create_user() কল করলে আমাদের লজিক কাজ করে।
# Settings Changeএই কোড লেখার পর settings.py তে অবশ্যই AUTH_USER_MODEL = 'myapp.User' লিখে দিতে হয়।

# ৩. ইন্টারভিউ প্রশ্ন ও উত্তর (নোট করে নিন)
# প্রশ্ন: BaseUserManager এর কাজ কী?
# উত্তর: এটি কোনো ডাটাবেস টেবিল নয়। এটি একটি হেল্পার ক্লাস যা নতুন ইউজার বা সুপারইউজার তৈরি করার পদ্ধতি (Method) ডিফাইন করে। 
# যেমন: ইমেইল নরমাল করা (ছোট হাতের অক্ষরে রূপান্তর) বা পাসওয়ার্ড এনক্রিপ্ট করা।

# প্রশ্ন: normalize_email কেন দরকার?
# উত্তর: ইউজারের ইমেইল যাতে ডুপ্লিকেট না হয়। 
# যেমন: Test@Gmail.Com আর test@gmail.com যেন একই ইউজার হিসেবে গণ্য হয়, তাই ইমেইলের ডোমেইন অংশকে ছোট হাতের অক্ষরে রূপান্তর করা হয়।

# প্রশ্ন: PermissionsMixin কেন যোগ করেছেন?
# উত্তর: এটি যোগ করলে জ্যাঙ্গোর ডিফল্ট পারমিশন সিস্টেম (Groups, Permissions) আমাদের কাস্টম মডেলের সাথে কাজ করবে। 
# এটি ছাড়া আপনি জ্যাঙ্গো এডমিন প্যানেলে ফুল এক্সেস পাবেন না।