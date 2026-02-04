from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products' # এখানে 'apps.' যোগ করতে হবে
    
    
# ইন্টারভিউতে বলতে পারেন: "আমি যখন অ্যাপটিকে apps/ সাব-ফোল্ডারে মুভ করেছি, তখন জ্যাঙ্গোর অ্যাপ রেজিস্ট্রিতে তার পাথ (Path) বদলে গেছে। 
# তাই আমাকে AppConfig-এ গিয়ে তার ফুল পাথ apps.products বলে দিতে হয়েছে যাতে জ্যাঙ্গো মডিউলটি লোড করতে পারে।"