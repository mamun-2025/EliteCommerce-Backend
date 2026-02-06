
from django.urls import path
from .views import CategoryListView, ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),

]
