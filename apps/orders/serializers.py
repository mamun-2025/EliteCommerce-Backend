
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = OrderItem
      fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
   items = OrderItemSerializer(many=True)

   class Meta:
      model = OrderItem
      fields = ['id', 'user', 'total_price', 'status', 'items', 'created_at']
      read_only_fields = ['user']

   def create(self, validate_data):
      items_data = validate_data.pop('items')
      user = self.context['request'].user
      order = Order.objects.create(user=user, **validate_data)
      for item_data in items_data:
         OrderItem.objects.create(order=order, **item_data)
      return order
   

