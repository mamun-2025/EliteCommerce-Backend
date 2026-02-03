
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# আমাদের তৈরি করা সিরিয়ালাইজারগুলো ইমপোর্ট করছি
from .serializers import UserRegistrationSerializer, UserProfileSerializer

# ১. ইউজার রেজিস্ট্রেশন ভিউ
class UserRegistrationView(APIView):
   def post(self, request):
      serializer = UserRegistrationSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

# ২. ইউজার প্রোফাইল ভিউ (লগইন করা ইউজারের জন্য)
class UserProfileView(APIView):
   permission_classes = [IsAuthenticated] # শুধুমাত্র লগইন করা ইউজার এক্সেস পাবে
   # request.user-এ বর্তমান ইউজারের অবজেক্ট থাকে যা টোকেন থেকে আসে
   def get(self, request):
      serializer = UserProfileSerializer(request.user)
      return Response(serializer.data)
   
   
   
      
