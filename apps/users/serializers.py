
from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
   password = serializers.CharField(write_only=True)

   class Meta:
      model = User
      fields = ['email', 'first_name', 'last_name', 'password']

   def create(self, validated_data):
      # সাধারণ ডিকশনারি থেকে পাসওয়ার্ড আলাদা করা
      password = validated_data.pop('password')
      # ইউজার অবজেক্ট তৈরি করা (পাসওয়ার্ড অটো হ্যাশ হবে কারণ আমরা create_user ম্যানেজার লিখেছিলাম)
      user = User.objects.create_user(password=password, **validated_data)
      return user
   
class UserProfileSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['id', 'email', 'first_name', 'last_name', 'is_staff']

      


