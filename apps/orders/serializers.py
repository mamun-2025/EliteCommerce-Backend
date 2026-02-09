
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = OrderItem
      fields = ['product', 'quantity', 'price']
      read_only_fields = ['price']

class OrderSerializer(serializers.ModelSerializer):
   items = OrderItemSerializer(many=True)

   class Meta:
      model = OrderItem
      fields = ['id', 'user', 'total_price', 'status', 'items', 'created_at']
      read_only_fields = ['user', 'status', 'total_price']

   def create(self, validate_data):
      items_data = validate_data.pop('items')
      user = self.context['request'].user

      # শুরুতে টোটাল প্রাইজ ০ ধরি
      total_price = 0
      order_items = []

      for item in items_data:
         product = item['product']
         quantity = item['quantity']
         price = product.price # প্রোডাক্ট টেবিল থেকে অটোমেটিক দাম নিল
         total_price += price * quantity
         order_items.append(OrderItem(product=product, quantity=quantity, price=price))

      # অর্ডার তৈরি
      order = Order.objects.create(user=user, total_price=total_price)

      # আইটেমগুলো একসাথে সেভ করা (Bulk Create)
      for item in order_items:
         item.order = order
         item.save()

      return order


