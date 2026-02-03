from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   # এডমিন প্যানেলের লিস্ট ভিউতে যা যা দেখাবে
   list_display = ('email', 'first_name', 'last_name', 'email', 'is_active', 'is_staff')
   # সার্চ বারে যা দিয়ে সার্চ করা যাবে
   search_fields = ('email', 'first_name', 'last_name')
   # ডিফল্ট শর্টিং (ইমেইল অনুযায়ী)
   ordering = ('email',)
