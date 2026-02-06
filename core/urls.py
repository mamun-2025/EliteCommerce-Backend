
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
   TokenObtainPairView, 
   TokenRefreshView,
)
from apps.users.views import UserRegistrationView, UserProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # লগইন করে টোকেন পাওয়ার জন্য
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # টোকেনের মেয়াদ শেষ হলে নতুন টোকেন পাওয়ার জন্য
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # নতুন ইউজার রেজিস্ট্রেশনের জন্য
    path('api/register/', UserRegistrationView.as_view(), name='user_registration'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
    path('api/products/', include('apps.products.urls')),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


